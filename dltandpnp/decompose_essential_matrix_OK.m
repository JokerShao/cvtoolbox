% This function decomposes the essential matrix E using svd decomposition
% In general, four possible poses exist for the decomposition of E.
% They are [R1,t], [R1,-t], [R2,t], [R2,-t].
%
% If E gives the epipolar constraint [p2;1]TA-TEA-1[p1;1]=0 between
% the image points p1 in the first image and p2 in second image,
% then any of the tuples [R1,t], [R1,-t], [R2,t], [R2,-t] is
% a change of basis from the first camera's coordinate system to
% the second camera's coordinate system.
% However, by decomposing E, one can only get the direction of the translation.
% For this reason, the translation t is returned with unit length.
% see: Multiple View Geometry 1st edition. P175 (Chinese).
%
% Input:   E       essential matrix [ 3 x 3 ]
% Output:  R1 R2   [ 3 x 3 ]
%          t       [ 3 x 1 ]
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.17

function [R1, R2, t] = decompose_essential_matrix_OK(E)

    [U, sigma, V] = svd(E, 'econ');
    W = [ 0 -1 0;
          1  0 0;
          0  0 1];
    R1 = U * W * V';
    R2 = U * W' * V';
    t = U(:,3);
end
