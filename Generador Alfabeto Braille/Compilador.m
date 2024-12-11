% Archivo: CorrerTodasLetras.m
% Este script ejecuta los archivos LetraA.m hasta LetraZ.m

% Generar las letras desde A hasta Z
%letras = 'A':'Z';

letras = 'A':'Z';

%Parámetros iniciales
num_train = 1000;
num_validation = 200;
num_test = 30;
image_size = 100; % Tamaño de la imagen 100x100
dotRadius = 8; % Radio del punto en píxeles
dotSpacing = 25; % Espaciado entre puntos en píxeles
dotCenters = [35, 35; 35, 60; 35, 85; 60, 35; 60, 60; 60, 85]; % Coordenadas Braille


for i = 1:length(letras)
    % Crear el nombre del archivo dinámicamente
    nombreArchivo = ['Letra', letras(i)];
    
    % Mostrar en pantalla cuál archivo se está ejecutando
    fprintf('Ejecutando archivo: %s.m\n', nombreArchivo);
    
    % Ejecutar el archivo
    run(nombreArchivo);
end

disp('Ejecución de todos los archivos completada.');