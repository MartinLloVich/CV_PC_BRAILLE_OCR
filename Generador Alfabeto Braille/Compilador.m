% Archivo: CorrerTodasLetras.m
% Este script ejecuta los archivos LetraA.m hasta LetraZ.m

% Generar las letras desde A hasta Z
letras = 'A':'Z';

for i = 1:length(letras)
    % Crear el nombre del archivo dinámicamente
    nombreArchivo = ['Letra', letras(i)];
    
    % Mostrar en pantalla cuál archivo se está ejecutando
    fprintf('Ejecutando archivo: %s.m\n', nombreArchivo);
    
    % Ejecutar el archivo
    run(nombreArchivo);
end

disp('Ejecución de todos los archivos completada.');