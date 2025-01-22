% Archivo: CorrerTodasLetras.m
% Este script ejecuta los archivos LetraA.m hasta LetraZ.m

% Generar las letras desde A hasta Z
%letras = 'A':'Z';

letras = 'A':'Z';

%Parámetros iniciales
num_train = 250;
num_validation = 70;
num_test = 10;
image_size = 640; % Tamaño de la imagen 100x100
dotRadius = 51; % Radio del punto en píxeles
dotSpacing = 96; % Espaciado entre puntos en píxeles
dotCenters = [224, 224; 224, 384; 224, 544; 384, 224; 384, 384; 384, 544]; % Coordenadas Braille


for i = 1:length(letras)
    % Crear el nombre del archivo dinámicamente
    nombreArchivo = ['Letra', letras(i)];

    % Mostrar en pantalla cuál archivo se está ejecutando
    fprintf('Ejecutando archivo: %s.m\n', nombreArchivo);

    % Ejecutar el archivo
    run(nombreArchivo);
end

disp('Ejecución de todos los archivos completada.');