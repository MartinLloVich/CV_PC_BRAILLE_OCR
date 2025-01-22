% Función para generar la imagen de Braille
function img = generate_braille_image(image_size, dotRadius, dotSpacing, dotCenters, gray_value, activatedDots)
    img = ones(image_size, image_size, 3); % Fondo blanco en RGB
    [x, y] = meshgrid(1:image_size, 1:image_size); % Coordenadas de la imagen
    for i = 1:size(dotCenters, 1)
        centerX = dotCenters(i, 1);
        centerY = dotCenters(i, 2);
        % Crear la máscara circular para el punto
        circleMask = (x - centerX).^2 + (y - centerY).^2 <= dotRadius^2;
        
        % Si el punto está activado, hacerlo rojo, de lo contrario gris claro
        if ismember(i, activatedDots)
            img(:, :, 1) = img(:, :, 1) .* ~circleMask + circleMask; % Canal rojo
            img(:, :, 2) = img(:, :, 2) .* ~circleMask; % Canal verde
            img(:, :, 3) = img(:, :, 3) .* ~circleMask; % Canal azul
        else
            img(:, :, 1) = img(:, :, 1) .* ~circleMask + circleMask * gray_value;
            img(:, :, 2) = img(:, :, 2) .* ~circleMask + circleMask * gray_value;
            img(:, :, 3) = img(:, :, 3) .* ~circleMask + circleMask * gray_value;
        end
    end
end
