pose1 = groundtruth(1,:);

nearest_pair = [groundtruth(:,1) vecnorm((groundtruth(:, 2:8) - pose1(2:8))')'];

nearest_pair = sortrows(nearest_pair, 2);

min_dist = 1e100;

pair_i = 0;
pair_j = 0;

for i = 2:size(groundtruth, 1)
    if (min_dist > norm(pose1(2:8) - groundtruth(i, 2:8)))
       min_dist = norm(pose1(2:8) - groundtruth(i, 2:8));
       pair_i = i;
    end
end

pair_i

