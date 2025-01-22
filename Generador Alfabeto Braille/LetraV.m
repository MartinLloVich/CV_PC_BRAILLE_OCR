

% Directorios de almacenamiento
image_dir = 'images/';
label_dir = 'labels/';

% Función para crear la imagen de la letra "V" en Braille
create_braille_image = @(gray_value) generate_braille_image(image_size, dotRadius, dotSpacing, dotCenters, gray_value, [1, 2, 3, 6]);

% Función para aplicar las transformaciones
apply_transformations = @(img) apply_random_transformations(img, image_size);

% Contador para el número de imágenes generadas
image_counter = 1;

% Crear imágenes de entrenamiento, validación y prueba
for i = 1:num_train + num_validation + num_test
    % Determinar el directorio y el tipo de imagen
    if i <= num_train
        img_dir = train_image_dir; % Carpeta para imágenes de entrenamiento
        label_dir_current = train_label_dir; % Carpeta para etiquetas de entrenamiento
    elseif i <= num_train + num_validation
        img_dir = validation_image_dir; % Carpeta para imágenes de validación
        label_dir_current = validation_label_dir; % Carpetas para etiquetas de validación
    else
        img_dir = test_image_dir; % Carpeta para imágenes de prueba
        label_dir_current = test_label_dir; % En test, a veces no se necesitan etiquetas, pero aquí las generamos.
    end
    
    % Crear la imagen base de la letra en Braille (gris claro)
    base_img = create_braille_image(1);
    
    % Aplicar transformaciones aleatorias
    transformed_img = apply_transformations(base_img);
    
    % Guardar la imagen en el directorio correspondiente
    img_filename = fullfile(img_dir, sprintf('v_%d.png', image_counter));
    imwrite(transformed_img, img_filename);
    
    % Crear el archivo de etiqueta en formato YOLO
    if ~isempty(label_dir_current)
        label_filename = fullfile(label_dir_current, sprintf('v_%d.txt', image_counter));
        
        % Detectar la región de la letra "A" en braille para calcular el bounding box
        % Asumimos que el braille es más claro que el fondo.
        threshold_level = 0.7; % Ajustar según el contraste de tu imagen
        bw = transformed_img > threshold_level;

        % Obtener las coordenadas del bounding box que encierra la región de interés
        stats = regionprops(bw, 'BoundingBox');
        
        if ~isempty(stats)
            % Si se detecta al menos una región, tomar la primera (en este caso, asumimos una sola letra)
            bbox = stats(1).BoundingBox; 
            % BoundingBox = [x, y, width, height] en pixeles
            % x,y: coord del píxel superior-izquierdo, width, height: en px
            
            % Convertir a formato YOLO
            img_h = size(transformed_img, 1);
            img_w = size(transformed_img, 2);
            
            % Coordenadas YOLO normalizadas
            x_center_norm = (bbox(1) + bbox(3)/2) / img_w;
            y_center_norm = (bbox(2) + bbox(4)/2) / img_h;
            width_norm = bbox(3) / img_w;
            height_norm = bbox(4) / img_h;
            
            % Clase de la letra
            class_id = 21;
            
            % Guardar la etiqueta
            fileID = fopen(label_filename, 'w');
            fprintf(fileID, '%d %.6f %.6f %.6f %.6f\n', class_id, x_center_norm, y_center_norm, width_norm, height_norm);
            fclose(fileID);
        end
    end
    
    % Incrementar el contador de imágenes
    image_counter = image_counter + 1;
end