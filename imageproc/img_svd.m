close all;


img = imread('../im.jpg');
gray_uint = rgb2gray(img);

figure;
imshow(img);

% figure;
% imshow(gray_uint);

gray = double(gray_uint);


[u, s, v] = svd(gray);

dimss = 300;

s_main = zeros(size(s));

s_main(1:dimss, 1:dimss) = s(1:dimss, 1:dimss);

gray_main = u*s_main*v';

gray_main_uint = uint8(gray_main);

mergeimg = [gray_uint gray_main_uint];
figure;
imshow(mergeimg);