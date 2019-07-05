
def print(name):
    import pandas as pd
    import json

    df = pd.read_csv("Task_3_Data_Export.csv")
    df = df[df['branch_id'] == name]

    df.rename(columns={'branch_id': 'Branch-id',
                       'branch_name': 'Branch name',
                       'class_name': 'Class',
                       'hlpid': 'Healpha id',
                       'section': 'Section',
                       'dental_gumhealth_vitality': 'dental_gumhealth-vitality',
                       'pickle_abdomen_shape': 'pickle_abdomen-shape',
                       'pickle_back_shape': 'pickle_back-shape',
                       'pickle_chest_shape': 'pickle_chest-shape',
                       'pickle_lowerlimbs_shape': 'pickle_lowerlimbs-shape',
                       'pickle_upperlimbs_shape': 'pickle_upperlimbs-shape',
                       'sysexam_respiratory_abnormsound_refres': 'sysexam_respiratory_abnormsound-refres',
                       'sysexam_respiratory_breahsoundbilateral_refres': 'sysexam_respiratory_breahsoundbilateral-refres',
                       'pickle_fingers_abnormalfingersColor': 'pickle_fingers_abnormalfingerscolor',
                       'pickle_lowerlimbs_swellingofjoints': 'pickle_lowerlimbs-swellingofjoints',
                       'pickle_upperlimbs_swellingofjoints': 'pickle_upperlimbs-swellingofjointse'}, inplace=True)

    df["middle_name"].fillna("", inplace=True)

    s = " "
    df["Full-name"] = df["first_name"] + s + df["middle_name"] + s + df["last_name"]

    col = list(df.columns.values)

    den_col = []
    hyg_col = []
    phy_col = []
    erg_col = []
    vitalscol = []
    entcol = []
    eyescol = []
    cols = ["Full-name", "Class", "Section", "Healpha id"]

    for i in col:
        if ((i.find("dental") == 0)):
            if (i.find("color") == -1):
                den_col.append(i)


        # for i in col:
        elif ((i.find("hygiene_") == 0)):
            if (i.find("color") == -1):
                hyg_col.append(i)


        # for i in col:
        elif ((i.find("pickle_") == 0)):
            if (i.find("color") == -1):
                phy_col.append(i)


        # for i in col:
        elif ((i.find("ergonomics") == 0)):
            if (i.find("color") == -1):
                erg_col.append(i)


        # for i in col:
        elif ((i.find("generic") == 0)):
            if ((i.find("color") == -1)):
                vitalscol.append(i)


        # for i in col:
        elif ((i.find("ent") == 0)):
            if ((i.find("color") == -1)):
                entcol.append(i)


        # for i in col:
        elif (i.find("eyes") == 0):
            if ((i.find("color") == -1)):
                eyescol.append(i)

    den_col = cols + den_col
    hyg_col = cols + hyg_col
    phy_col = cols + phy_col
    erg_col = cols + erg_col
    vitalscol = cols + vitalscol
    entcol = cols + entcol
    eyescol = cols + eyescol

    den_data = df[den_col]

    hyg_data = df[hyg_col]

    phy_data = df[phy_col]

    erg_data = df[erg_col]

    vitalsdata = df[vitalscol]

    entdata = df[entcol]

    eyesdata = df[eyescol]

    den_names = []
    for i in range(0, len(den_col)):
        x = den_col[i].split("_")[-1]
        x = x.capitalize()
        den_names.append(x)

    hyg_names = []
    for i in range(0, len(hyg_col)):
        x = hyg_col[i].split("_")[-1]
        x = x.capitalize()
        hyg_names.append(x)

    phy_names = []
    for i in range(0, len(phy_col)):
        if (phy_col[i].find('sysexam') == 0):
            x = ' '.join(phy_col[i].split("_")[-2:])
            x = x.capitalize()
            phy_names.append(x)
        else:
            x = phy_col[i].split("_")[-1]
            x = x.capitalize()
            phy_names.append(x)

    erg_names = []
    for i in range(0, len(erg_col)):
        x = erg_col[i].split("_")[-1]
        x = x.capitalize()
        erg_names.append(x)

    vitalsnames = []
    for i in range(0, len(vitalscol)):
        x = vitalscol[i].split("_")[-1]
        x = x.capitalize()
        vitalsnames.append(x)

    entnames = []
    for i in range(0, len(entcol)):
        x = ' '.join(entcol[i].split("_")[-2:])
        x = x.capitalize()
        entnames.append(x)

    eyesnames = []
    for i in range(0, len(eyescol)):
        x = ' '.join(eyescol[i].split("_")[-2:])
        x = x.capitalize()
        eyesnames.append(x)

    den_data.columns = den_names

    hyg_data.columns = hyg_names

    phy_data.columns = phy_names

    erg_data.columns = erg_names

    vitalsdata.columns = vitalsnames

    entdata.columns = entnames

    eyesdata.columns = eyesnames

    vitalsdata.rename(columns={'Height': 'Height (cm)',
                               'Weight': 'Weight (kg)',
                               'Bmi': 'Bmi (kg/m^2)',
                               'Bpdiastolic': 'Bpdiastolic (mm/Hg)',
                               'Bpsystolic': 'Bpsystolic (mm/Hg)',
                               'Oxygensat': 'Oxygensat (%)',
                               'Pulserate': 'Pulserate (/min)',
                               'Respiratoryrate': 'Respiratoryrate (/min)',
                               'Spirometer': 'Spirometer (liters/min)',
                               'Temp': 'Temp (F)'}, inplace=True)

    x = den_data.to_json(orient='split')
    y = hyg_data.to_json(orient='split')
    z = phy_data.to_json( orient='split')
    a = erg_data.to_json(orient='split')
    b = vitalsdata.to_json(orient='split')
    c = entdata.to_json(orient='split')
    d = eyesdata.to_json(orient='split')

    x = json.loads(x)
    y = json.loads(y)
    z = json.loads(z)
    a = json.loads(a)
    b = json.loads(b)
    c = json.loads(c)
    d = json.loads(d)



    def sort(test):
        c = []
        for i in test['columns']:
            c.append({"text": i})

        a = []
        b = []
        for i in test['data']:
            for j in i:
                b.append({"text": j})
            a.append(b)
            b = []
        return ([c] + a)

    x=sort(x)
    y=sort(y)
    z=sort(z)
    a=sort(a)
    b=sort(b)
    c=sort(c)
    d=sort(d)

    k={"dental": x, "hygiene": y, "physical": z, "ergonomics": a, "vital" : b, "ent" : c,
     'eyes' : d}

    return (k)




