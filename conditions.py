if ((class_name == 'all') & (section != 'all') & (gender != 'all')):
        d_var = d_data[(d_data[(d_data['section'] == section) & (d_data['gender'] == gender)] == 0) | (d_data[(d_data['section'] == section) & (d_data['gender'] == gender)] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[(e_data['section'] == section) & (e_data['gender'] == gender)] == 0) | (e_data[(e_data['section'] == section) & (e_data['gender'] == gender)] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[(v_data['section'] == section) & (v_data['gender'] == gender)] == 0) | (v_data[(v_data['section'] == section) & (v_data['gender'] == gender)] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[(h_data['section'] == section) & (h_data['gender'] == gender)] == 0) | (h_data[(h_data['section'] == section) & (h_data['gender'] == gender)] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[(p_data['section'] == section) & (p_data['gender'] == gender)] == 0) | (p_data[(p_data['section'] == section) & (p_data['gender'] == gender)] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[(eye_data['section'] == section) & (eye_data['gender'] == gender)] == 0) | (eye_data[(eye_data['section'] == section) & (eye_data['gender'] == gender)] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[(ergo_data['section'] == section) & (ergo_data['gender'] == gender)] == 0) | (ergo_data[(ergo_data['section'] == section) & (ergo_data['gender'] == gender)] == 0.5)].count(axis = 1)

    elif ((section == 'all') & (class_name != 'all') & (gender != 'all')):
        d_var = d_data[(d_data[(d_data['class_name'] == class_name) & (d_data['gender'] == gender)] == 0) | (d_data[(d_data['class_name'] == class_name) & (d_data['gender'] == gender)] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[(e_data['class_name'] == class_name) & (e_data['gender'] == gender)] == 0) | (e_data[(e_data['class_name'] == class_name) & (e_data['gender'] == gender)] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[(v_data['class_name'] == class_name) & (v_data['gender'] == gender)] == 0) | (v_data[(v_data['class_name'] == class_name) & (v_data['gender'] == gender)] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[(h_data['class_name'] == class_name) & (h_data['gender'] == gender)] == 0) | (h_data[(h_data['class_name'] == class_name) & (h_data['gender'] == gender)] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[(p_data['class_name'] == class_name) & (p_data['gender'] == gender)] == 0) | (p_data[(p_data['class_name'] == class_name) & (p_data['gender'] == gender)] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['gender'] == gender)] == 0) | (eye_data[(eye_data['class_name'] == class_name) & (eye_data['gender'] == gender)] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[(ergo_data['class_name'] == class_name) & (ergo_data['gender'] == gender)] == 0) | (ergo_data[(ergo_data['class_name'] == class_name) & (ergo_data['gender'] == gender)] == 0.5)].count(axis = 1)

    elif ((section != 'all') & (class_name != 'all') & (gender == 'all')):
        d_var = d_data[(d_data[(d_data['class_name'] == class_name) & (d_data['section'] == section)] == 0) | (d_data[(d_data['class_name'] == class_name) & (d_data['section'] == section)] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[(e_data['class_name'] == class_name) & (e_data['section'] == section)] == 0) | (e_data[(e_data['class_name'] == class_name) & (e_data['section'] == section)] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[(v_data['class_name'] == class_name) & (v_data['section'] == section)] == 0) | (v_data[(v_data['class_name'] == class_name) & (v_data['section'] == section)] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[(h_data['class_name'] == class_name) & (h_data['section'] == section)] == 0) | (h_data[(h_data['class_name'] == class_name) & (h_data['section'] == section)] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[(p_data['class_name'] == class_name) & (p_data['section'] == section)] == 0) | (p_data[(p_data['class_name'] == class_name) & (p_data['section'] == section)] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section)] == 0) | (eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section)] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[(ergo_data['class_name'] == class_name) & (ergo_data['section'] == section)] == 0) | (ergo_data[(ergo_data['class_name'] == class_name) & (ergo_data['section'] == section)] == 0.5)].count(axis = 1)

    elif (class_name == 'all') & (section == 'all') & (gender != 'all'):
        d_var = d_data[(d_data[d_data['gender'] == gender] == 0) | (d_data[d_data['gender'] == gender] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[e_data['gender'] == gender] == 0) | (e_data[e_data['gender'] == gender] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[v_data['gender'] == gender] == 0) | (v_data[v_data['gender'] == gender] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[h_data['gender'] == gender] == 0) | (h_data[h_data['gender'] == gender] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[p_data['gender'] == gender] == 0) | (p_data[p_data['gender'] == gender] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[eye_data['gender'] == gender] == 0) | (eye_data[eye_data['gender'] == gender] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[ergo_data['gender'] == gender] == 0) | (ergo_data[ergo_data['gender'] == gender] == 0.5)].count(axis = 1)

    elif (class_name == 'all') & (gender == 'all') & (section != 'all'):
        d_var = d_data[(d_data[d_data['section'] == section] == 0) | (d_data[d_data['section'] == section] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[e_data['section'] == section] == 0) | (e_data[e_data['section'] == section] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[v_data['section'] == section] == 0) | (v_data[v_data['section'] == section] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[h_data['section'] == section] == 0) | (h_data[h_data['section'] == section] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[p_data['section'] == section] == 0) | (p_data[p_data['section'] == section] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[eye_data['section'] == section] == 0) | (eye_data[eye_data['section'] == section] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[ergo_data['section'] == section] == 0) | (ergo_data[ergo_data['section'] == section] == 0.5)].count(axis = 1)

    elif (section == 'all') & (gender == 'all') & (class_name != 'all'):
        d_var = d_data[(d_data[d_data['class_name'] == class_name] == 0) | (d_data[d_data['class_name'] == class_name] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[e_data['class_name'] == class_name] == 0) | (e_data[e_data['class_name'] == class_name] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[v_data['class_name'] == class_name] == 0) | (v_data[v_data['class_name'] == class_name] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[h_data['class_name'] == class_name] == 0) | (h_data[h_data['class_name'] == class_name] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[p_data['class_name'] == class_name] == 0) | (p_data[p_data['class_name'] == class_name] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[eye_data['class_name'] == class_name] == 0) | (eye_data[eye_data['class_name'] == class_name] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[ergo_data['class_name'] == class_name] == 0) | (ergo_data[ergo_data['class_name'] == class_name] == 0.5)].count(axis = 1)

    elif ((class_name == 'all') & (section == 'all') & (gender == 'all')):
        d_var = d_data[(d_data == 0) | (d_data == 0.5)].count(axis = 1)
        e_var = e_data[(e_data == 0) | (e_data == 0.5)].count(axis = 1)
        v_var = v_data[(v_data == 0) | (v_data == 0.5)].count(axis = 1)
        h_var = h_data[(h_data == 0) | (h_data == 0.5)].count(axis = 1)
        p_var = p_data[(p_data == 0) | (p_data == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data == 0) | (eye_data == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data == 0) | (ergo_data == 0.5)].count(axis = 1)

    else:
        d_var = d_data[(d_data[(d_data['class_name'] == class_name) & (d_data['section'] == section ) & (d_data['gender'] == gender)] == 0) |
                       (d_data[(d_data['class_name'] == class_name) & (d_data['section'] == section ) & (d_data['gender'] == gender)] == 0.5)].count(axis = 1)
        e_var = e_data[(e_data[(e_data['class_name'] == class_name) & (e_data['section'] == section ) & (e_data['gender'] == gender)] == 0) |
                       (e_data[(e_data['class_name'] == class_name) & (e_data['section'] == section ) & (e_data['gender'] == gender)] == 0.5)].count(axis = 1)
        v_var = v_data[(v_data[(v_data['class_name'] == class_name) & (v_data['section'] == section ) & (v_data['gender'] == gender)] == 0) |
                       (v_data[(v_data['class_name'] == class_name) & (v_data['section'] == section ) & (v_data['gender'] == gender)] == 0.5)].count(axis = 1)
        h_var = h_data[(h_data[(h_data['class_name'] == class_name) & (h_data['section'] == section ) & (h_data['gender'] == gender)] == 0) |
                       (h_data[(h_data['class_name'] == class_name) & (h_data['section'] == section ) & (h_data['gender'] == gender)] == 0.5)].count(axis = 1)
        p_var = p_data[(p_data[(p_data['class_name'] == class_name) & (p_data['section'] == section ) & (p_data['gender'] == gender)] == 0) |
                       (p_data[(p_data['class_name'] == class_name) & (p_data['section'] == section ) & (p_data['gender'] == gender)] == 0.5)].count(axis = 1)
        eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section ) & (eye_data['gender'] == gender)] == 0) |
                       (eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section ) & (eye_data['gender'] == gender)] == 0.5)].count(axis = 1)
        ergo_var = ergo_data[(ergo_data[(ergo_data['class_name'] == class_name) & (ergo_data['section'] == section ) & (ergo_data['gender'] == gender)] == 0) |
                       (ergo_data[(ergo_data['class_name'] == class_name) & (ergo_data['section'] == section ) & (ergo_data['gender'] == gender)] == 0.5)].count(axis = 1)

    d_index = [list(d_var[d_var == i].index) if i!= 3 else list(d_var[d_var >= 3].index) for i in range(1,4)]
    e_index = [list(e_var[e_var == i].index) if i!= 3 else list(e_var[e_var >= 3].index) for i in range(1,4)]
    v_index = [list(v_var[v_var == i].index) if i!= 3 else list(v_var[v_var >= 3].index) for i in range(1,4)]
    h_index = [list(h_var[h_var == i].index) if i!= 3 else list(h_var[h_var >= 3].index) for i in range(1,4)]
    p_index = [list(p_var[p_var == i].index) if i!= 3 else list(p_var[p_var >= 3].index) for i in range(1,4)]
    eye_index = [list(eye_var[eye_var == i].index) if i!= 3 else list(eye_var[eye_var >= 3].index) for i in range(1,4)]
    ergo_index = [list(ergo_var[ergo_var == i].index) if i!= 3 else list(ergo_var[ergo_var >= 3].index) for i in range(1,4)]
    phy_ergo_hyg_index = [list(set(x+y+z)) for x,y,z in zip(p_index, h_index, ergo_index)]

