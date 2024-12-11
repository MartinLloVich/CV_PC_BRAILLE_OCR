function transformed_img = apply_random_transformations(img, image_size)
    transformed_img = img;
    
    % Aplicar traslación aleatoria con fondo blanco
    tx = randi([-10, 10]);
    ty = randi([-10, 10]);
    transformed_img = imtranslate(transformed_img, [tx, ty], 'FillValues', 1);

    % Aplicar rotación aleatoria con fondo blanco
    angle = randi([-15, 15]); % Ángulo de rotación entre -15 y 15 grados
    transformed_img = imrotate(transformed_img, angle, 'bilinear', 'crop');
    
    % Ajustar brillo aleatorio
    brightness_factor = 0.5 + rand * 0.5; % Factor de brillo entre 0.5 y 1
    transformed_img = transformed_img * brightness_factor;
    transformed_img = min(transformed_img, 1); % Limitar valores entre 0 y 1
end

