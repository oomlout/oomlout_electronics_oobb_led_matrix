import oom_kicad
import working_opsc


base = {}

base['name'] = 'oomlout_oobb_led_matrix'
base['description'] = 'an electronics project that is an led matrix in the oobb shape, current version is 3 x 10 oobb with 6 columns and 15 rows of leds, it uses the aip1640 16 x 8 driver chip'



def main():
    components = set_components()
    oom_kicad.generate_outputs()
    oom_kicad.generate_readme(**base)

    make_solder_jig(components=components)


def set_components():
    pass
    board_file = rf'oomp/current_version/working/working.kicad_pcb'
    components = []
    component = {}
    #go through an array 6 wide and 15 high mage a countyer that starts at 1 and is incrmented each time
    start_x  = -18.75
    start_y = -52.5
    spacing_x = 7.5
    spacing_y = 7.5
    counter = 1
    for i in range(15):
        for j in range(6):
            component = {}
            component['reference'] = f'L{counter}'
            x = start_x + (j * spacing_x) -0.866
            y = start_y + (i * spacing_y) -0.866
            correl_pos = oom_kicad.get_from_corel_coord(x,y)
            component['position'] = (correl_pos[0], correl_pos[1], 45)
            
            components.append(component)
            counter += 1
            
    component = {}
    component['reference'] = 'U1'
    corel_pos = oom_kicad.get_from_corel_coord(0, -65)
    component['position'] = (corel_pos[0], corel_pos[1], 0)
    components.append(component)

    #mouning holes
    #H1 - H5 are m6
    x = [-15,0,15]
    y = [-67.5,67.5]
    components.append({"reference":"H1","position":(x[0],y[0]),"corel_pos":True})
    components.append({"reference":"H2","position":(x[2],y[0]),"corel_pos":True})
    components.append({"reference":"H3","position":(x[0],y[1]),"corel_pos":True})
    components.append({"reference":"H4","position":(x[1],y[1]),"corel_pos":True})
    components.append({"reference":"H5","position":(x[2],y[1]),"corel_pos":True})
    #h8 - 16 are m3
    x = [-15,-7.5,0,7.5,15]
    y = [-67.5,-60,60,67.5]
    #components.append({"reference":"H6","position":(x[1],y[0]),"corel_pos":True})
    #components.append({"reference":"H7","position":(x[3],y[0]),"corel_pos":True})
    #components.append({"reference":"H8","position":(x[0],y[1]),"corel_pos":True})
    #components.append({"reference":"H9","position":(x[4],y[1]),"corel_pos":True})
    components.append({"reference":"H10","position":(x[0],y[2]),"corel_pos":True})
    components.append({"reference":"H11","position":(x[1],y[2]),"corel_pos":True})
    components.append({"reference":"H12","position":(x[2],y[2]),"corel_pos":True})
    components.append({"reference":"H13","position":(x[3],y[2]),"corel_pos":True})
    components.append({"reference":"H14","position":(x[4],y[2]),"corel_pos":True})
    components.append({"reference":"H15","position":(x[1],y[3]),"corel_pos":True})
    components.append({"reference":"H16","position":(x[3],y[3]),"corel_pos":True})


    oom_kicad.kicad_set_components(board_file=board_file, components=components)


    return components

def make_solder_jig(**kwargs):
    pass
    working_opsc.main(**kwargs)


if __name__ == '__main__':
    main()