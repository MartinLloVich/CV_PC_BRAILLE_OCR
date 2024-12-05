% Parámetros iniciales
num_train = 40;
num_validation = 25;
num_test = 10;
image_size = 100; % Tamaño de la imagen 100x100
dotRadius = 8; % Radio del punto en píxeles
dotSpacing = 25; % Espaciado entre puntos en píxeles
dotCenters = [35, 35; 35, 60; 35, 85; 60, 35; 60, 60; 60, 85]; % Coordenadas Braille

% Directorios de almacenamiento
image_dir = 'images/';
label_dir = 'labels/';

% Función para crear la imagen de la letra "F" en Braille
create_braille_image = @(gray_value) generate_braille_image(image_size, dotRadius, dotSpacing, dotCenters, gray_value, [1, 2, 4]);

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
        label_dir_current = validation_label_dir; % Carpeta para etiquetas de validación
    else
        img_dir = test_image_dir; % Carpeta para imágenes de prueba
        label_dir_current = ''; % No se requiere etiquetas para test
    end
    
    % Crear la imagen base de la letra "F" en Braille (gris claro)
    base_img = create_braille_image(0.8);
    
    % Aplicar transformaciones aleatorias
    transformed_img = apply_transformations(base_img);
    
    % Guardar la imagen en el directorio correspondiente
    img_filename = fullfile(img_dir, sprintf('f_%d.png', image_counter));
    imwrite(transformed_img, img_filename);
    
    % Crear el archivo de etiqueta en formato YOLO
    if ~isempty(label_dir_current)
        label_filename = fullfile(label_dir_current, sprintf('f_%d.txt', image_counter));
        fileID = fopen(label_filename, 'w');
        
        % La clase de la letra "F" es 5
        class_id = 5;

        % Escribir los datos en el archivo de etiquetas en formato YOLO
        fprintf(fileID, '%d %.6f %.6f %.6f %.6f\n', class_id, 0.50000, 0.500000, 0.8500000, 0.850000);
        
        fclose(fileID);
    end
    
    % Incrementar el contador de imágenes
    image_counter = image_counter + 1;
end