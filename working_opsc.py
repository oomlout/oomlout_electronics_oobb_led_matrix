import opsc
import oobb as ob

save_type = "none"
#save_type = "all"

def main(**kwargs):
    if type not in kwargs:        
        kwargs["type"] = "project"
    thing = ob.get_default_thing(**kwargs)

    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)
    thickness = kwargs.get("thickness", 3)

    th = thing["components"]

    plate_pos = [0, 0, -1]

    #add plate
    #th.extend(get_holder_electronics_base_03_03(**kwargs))
    #add oobb_pl
    th.extend(ob.oe(t="p", s="oobb_pl", holes=False, width=width, height=height, depth_mm=thickness, pos=plate_pos, mode="all"))
    #add u holes
    th.extend(ob.oobb_easy(t="n", s="oobb_holes", width=width, height=height, radius_name="m6", holes=["bottom","top","left","right"], pos=plate_pos, m=""))
    th.extend(ob.oobb_easy(t="n", s="oobe_holes", width=(width*2)-1, height=(height*2)-1, radius_name="m3", holes=["bottom","top","left","right"], pos=plate_pos, m=""))
    led_pos = [0, 0, 0]
    deets = ob.oobb_easy(t="n", s="oobb_oomp_l5", pos=led_pos, m="#")
    th.append(deets)






    ob.build_thing_filename(thing=thing["components"], save_type=save_type, filename="opsc/current_version/working/working")



if __name__ == "__main__":
    main()