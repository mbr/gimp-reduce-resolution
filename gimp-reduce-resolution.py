#!/usr/bin/python

from gimpfu import *

def python_reduce_resolution(timg, tdrawable, x_res, y_res, y_equal_x):
    pdb.gimp_image_undo_group_start(timg)

    # ui-hack
    if y_equal_x:
        y_res = x_res

    # get resolution and calculate necessary scaling
    res = pdb.gimp_image_get_resolution(timg)
    scale_x, scale_y = float(x_res)/res[0], float(y_res)/res[1]

    # scale image to new size
    timg.scale(
        int(round(timg.width*scale_x)),
        int(round(timg.height*scale_y))
    )

    # fix resolution
    pdb.gimp_image_set_resolution(timg, x_res, y_res)

    pdb.gimp_image_undo_group_end(timg)


register("python_fu_change_resolution",
         "Reduce the print resolution of an image while maintaining its dimensions",
         "Reduce the print resolution of an image while maintaining its dimensions",
         "Marc Brinkmann",
         "Marc Brinkmann",
         "2012",
         "<Image>/Image/Reduce Resol_ution",
         "*",
         [
              (PF_INT, "x_res", "New X Resolution", 72),
                (PF_INT, "y_res", "New Y Resolution", 72),
              (PF_BOOL, "y_equal_x", "Ignore Y Resolution and use X instead", True)
         ],
         [],
         python_reduce_resolution
         )

main()
