"""
空间直线与平面交点计算

author:       Zexi Shao
date:         2025.04.28
last modify:  2025.04.28
"""
import numpy as np
import pyvista as pv


def random_line():
    ''' 生成射线：随机起点 + 单位方向向量
    '''
    origin = np.random.rand(3, 1) * 2 - 1
    direction = np.random.randn(3, 1)
    direction /= np.linalg.norm(direction)
    return origin, direction

def random_plane():
    ''' 生成平面：随机平面上一点 + 单位法向量
    '''
    plane_point = np.random.rand(3, 1) * 2 - 1
    plane_normal = np.random.randn(3, 1)
    plane_normal /= np.linalg.norm(plane_normal)
    return plane_point, plane_normal

def intersect_line_plane(origin, direction, plane_point, plane_normal, eps=1e-6):
    ''' 计算射线与平面的交点，平行时返回 None
        input: 3 x 1
    '''
    # 分母 denominator
    denom = plane_normal.transpose().dot(direction)
    if abs(denom) < eps:
        return None
    t = plane_normal.transpose().dot(plane_point - origin) / denom
    return origin + direction * t


if __name__ == '__main__':

    # 生成随机射线
    origin, direction = random_line()
    origin, direction = np.array([0., 0., 0.]).reshape(3, 1), np.array([1., 1., 1.]).reshape(3, 1)
    direction /= np.linalg.norm(direction)

    # 生成随机平面
    plane_point, plane_normal = random_plane()
    # xoy平面
    plane_point, plane_normal = np.array([0., 0., 0.]).reshape(3, 1), np.array([0., 0., 1.]).reshape(3, 1)
    pt = intersect_line_plane(origin, direction, plane_point, plane_normal)

    # 可视化
    plotter = pv.Plotter(window_size=[800,600])

    # 平面
    plane = pv.Plane(center=plane_point.transpose(),
                    direction=plane_normal.transpose(),
                    i_size=3.0, j_size=3.0,
                    i_resolution=20, j_resolution=20)
    plotter.add_mesh(plane, color='lightblue', opacity=0.6, show_edges=True)

    # 空间向量：用直线段表示
    line_length = 3.0  # 可调整直线段长度
    end_point = origin + direction * line_length
    line = pv.Line(pointa=origin.transpose(), pointb=end_point.transpose(), resolution=1)
    plotter.add_mesh(line, line_width=4, color='red')

    # 如果存在交点，用球标记
    if pt is not None:
        sphere = pv.Sphere(radius=0.05, center=pt)
        plotter.add_mesh(sphere, color='green')

    plotter.add_axes()   
    plotter.show_grid()
    plotter.show(title="Line-Plane Intersection (Line Representation)")

