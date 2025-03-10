import open3d as o3d
import numpy as np
'''
can find the help for the open3d library.
http://www.open3d.org/docs/release/python_api/open3d.io.html

'''


list=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
pc1 = o3d.geometry.PointCloud()
pc1.points = o3d.utility.Vector3dVector(list)
o3d.visualization.draw_geometries([pc1])
print(pc1)

# list_face = [()]


# pc =o3d.io.read_point_cloud('skull.ply')
# o3d.visualization.draw_geometries([pc])
# pc_points=np.asarray(pc.points)
# pc_colors=np.asarray(pc.colors)
# pc_normal = np.asarray(pc.normals)
o3d.io.write_point_cloud('point.ply',pc1)