def expand(sel_branch,class_name,section,gender):
    import pandas as pd
    import numpy as np
    dic={}
    df = pd.read_csv("branch_Wise.csv", keep_default_na=False)
    df = df[df.generic_tempcolor != 'null']
    df.replace(' ', np.nan, inplace=True)
    df.replace('', np.nan, inplace=True)
    df.replace('null', np.nan, inplace=True)

    to_keep = df[['hlpid','class_name', 'school_name', 'section', 'gender', 'first_name', 'middle_name', 'last_name','created_date', 'branch_id']]
    df = df.drop( ['hlpid', 'class_name', 'school_name', 'section', 'gender', 'first_name', 'middle_name', 'last_name','created_date', 'branch_id'], axis=1).apply(pd.to_numeric)
    df = pd.concat([df, to_keep], axis=1)

    if(sel_branch=='all'):
        vit_cols = []
        for k in df.columns:
            if ((k.find("generic") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                vit_cols.append(k)
        vital_fields_new = ['BMI', 'BP (Systolic)', 'BP (Diastolic)', 'Height',
                            'Oxygensaturation',
                            'Pulserate', 'Respiratoryrate', 'Spirometer', 'Temperature', 'Weight','class_name','section','gender']
        vit_data = df[vit_cols]
        vit_data.columns = vital_fields_new
        # vit_no = df[vit_cols][(df[vit_cols] == '0') | (df[vit_cols] == '0.5')].count(axis=1)
        # vit_atleast1 = vit_no[vit_no >= 1].count()
        phy_cols = []
        for k in df.columns:
            if ((k.find("pickle") == 0) | (k.find("sysexam") == 0) | (k.find("gender") == 0) | (
                    k.find("class_name") == 0) | (k.find("section") == 0)):
                phy_cols.append(k)
        phy_fields_new = ['Abdomen', 'Back', 'Chest', 'Clubbing', 'Cyanosis', 'Edema',
                          'AbnormalFingers', 'ExtraFingers', 'FusedFingers', 'Icterus', 'Koilonychia', 'Lowershape',
                          'LowerSwellingOfJoints', 'Lymphadenopathy', 'Pallor', 'Thyroid', 'AbnormalToes', 'ExtraToes',
                          'FusedToes', 'UpperShape', 'UpperSwellingOfJoint', 'Abdominaldistention', 'Hernia',
                          'Liver', 'Mass', 'Scars', 'Spleen', 'VisibleBloodVessels', 'Cardiores', 'Murmur',
                          'CranialNerves','MentalStatusTesting', 'Power', 'Reflexes', 'Sensation', 'Tone', 'Respres', 'Breathres','class_name','section','gender']
        phy_data = df[phy_cols]
        phy_data.columns = phy_fields_new
        ergonomics_cols = []
        for k in df.columns:
            if ((k.find("ergonomics_") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                ergonomics_cols.append(k)
        ergonomics_fields_new = [ 'JointMovements', 'MuscleStrength', 'OverallBone','class_name','section','gender']
        erg_data = df[ergonomics_cols]
        erg_data.columns = ergonomics_fields_new
        hyg_cols = []
        for k in df.columns:
            if ((k.find("hygiene") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                hyg_cols.append(k)
        hyg_fields_new = ['HairColour', 'HairCondition', 'HairDandruff', 'HairLice', 'Nails', 'SkinCondition', 'SkinRash','class_name','section','gender']
        hyg_data = df[hyg_cols]
        hyg_data.columns = hyg_fields_new

        # phy_no = df[phy_cols][(df[phy_cols] == '0') | (df[phy_cols] == '0.5')].count(axis=1)
        # erg_no = df[ergonomics_cols][(df[ergonomics_cols] == '0') | (df[ergonomics_cols] == '0.5')].count(axis=1)
        # hyg_no = df[hyg_cols][(df[hyg_cols] == '0') | (df[hyg_cols] == '0.5')].count(axis=1)
        # phy_atl = phy_no[phy_no >= 1].index
        # erg_atl = erg_no[erg_no >= 1].index
        # hyg_atl = hyg_no[hyg_no >= 1].index
        # phy_final = list(set(phy_atl) | set(hyg_atl) | set(erg_atl))
        # phy_final = set(phy_final)
        # phy_atleast1 = len(phy_final)

        dent_cols = []
        for k in df.columns:
            if ((k.find("dental") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (k.find("section") == 0)):
                dent_cols.append(k)
        dental_fields_new = ['Bleeding', 'Impaction', 'Inflamation', 'Teethcondition', 'Gum Vitality', 'Alignment',
                             'Badbreath', 'Cavities', 'Plaque', 'Strains', 'Tarter', 'Dental Vitality', 'class_name',
                             'gender', 'section']
        dent_data = df[dent_cols]
        dent_data.columns = dental_fields_new
        # dent_no = df[dent_cols][(df[dent_cols] == '0') | (df[dent_cols] == '0.5')].count(axis=1)
        # dent_atleast1 = dent_no[dent_no >= 1].count()
        ent_cols = []
        for k in df.columns:
            if ((k.find("ent_") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                ent_cols.append(k)
        ent_fields_new = [ 'LeftDischarge', 'LeftHygiene', 'LeftPerforation', 'LeftPinna', 'LeftPit',
                          'LeftWaxImpacted', 'RightDischarge', 'RightHygiene', 'RightPerforation', 'RightPinnacolor',
                          'RightPitcolor', 'RightWaxImpacted', 'LeftHypertrophideturbinate',
                          'RightHypertrophideturbinate', 'Thrush', 'Tongueglossitis', 'Tonguetie', 'Tonsils','class_name','section','gender']
        ent_data = df[ent_cols]
        ent_data.columns = ent_fields_new
        # ent_no = df[ent_cols][(df[ent_cols] == '0') | (df[ent_cols] == '0.5')].count(axis=1)
        # ent_atleast1 = ent_no[ent_no >= 1].count()
        eye_cols = []
        for k in df.columns:
            if ((k.find("eyes") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                eye_cols.append(k)
        eye_fields_new = [ 'AbnormalEyeMovement', 'Anisocoria', 'Anisometropia', 'Astigmatism',
                          'Bitotspots',
                          'Cornealscar', 'Gazeasymmetry', 'Hyperopia', 'Myopia', 'Squint', 'VisionScreeningResult',
                          'Wearglass','class_name','section','gender']
        eye_data = df[eye_cols]
        eye_data.columns = eye_fields_new
        # eye_no = df[eye_cols][(df[eye_cols] == '0') | (df[eye_cols] == '0.5')].count(axis=1)
        # eye_atleast1 = eye_no[eye_no >= 1].count()
        if ((class_name == 'all') & (section != 'all') & (gender != 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[(dent_data['section'] == section) & (dent_data['gender'] == gender)] == 0) | (dent_data[(dent_data['section'] == section) & (dent_data['gender'] == gender)] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[(ent_data['section'] == section) & (ent_data['gender'] == gender)] == 0) | (ent_data[(ent_data['section'] == section) & (ent_data['gender'] == gender)] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[(vit_data['section'] == section) & (vit_data['gender'] == gender)] == 0) | (vit_data[(vit_data['section'] == section) & (vit_data['gender'] == gender)] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[(hyg_data['section'] == section) & (hyg_data['gender'] == gender)] == 0) | (hyg_data[(hyg_data['section'] == section) & (hyg_data['gender'] == gender)] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[(phy_data['section'] == section) & (phy_data['gender'] == gender)] == 0) | (phy_data[(phy_data['section'] == section) & (phy_data['gender'] == gender)] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[(eye_data['section'] == section) & (eye_data['gender'] == gender)] == 0) | (eye_data[(eye_data['section'] == section) & (eye_data['gender'] == gender)] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[(erg_data['section'] == section) & (erg_data['gender'] == gender)] == 0) | (erg_data[(erg_data['section'] == section) & (erg_data['gender'] == gender)] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100,2)
            e_var = round(e_var / total * 100,2)
            v_var = round(v_var / total * 100,2)
            h_var = round(h_var / total * 100,2)
            p_var = round(p_var / total * 100,2)
            eye_var = round(eye_var / total * 100,2)
            ergo_var = round(ergo_var / total * 100,2)


        elif ((section == 'all') & (class_name != 'all') & (gender != 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[(dent_data['class_name'] == class_name) & (dent_data['gender'] == gender)] == 0) | (dent_data[(dent_data['class_name'] == class_name) & (dent_data['gender'] == gender)] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[(ent_data['class_name'] == class_name) & (ent_data['gender'] == gender)] == 0) | (ent_data[(ent_data['class_name'] == class_name) & (ent_data['gender'] == gender)] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[(vit_data['class_name'] == class_name) & (vit_data['gender'] == gender)] == 0) | (vit_data[(vit_data['class_name'] == class_name) & (vit_data['gender'] == gender)] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['gender'] == gender)] == 0) | (hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['gender'] == gender)] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[(phy_data['class_name'] == class_name) & (phy_data['gender'] == gender)] == 0) | (phy_data[(phy_data['class_name'] == class_name) & (phy_data['gender'] == gender)] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['gender'] == gender)] == 0) | (eye_data[(eye_data['class_name'] == class_name) & (eye_data['gender'] == gender)] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[(erg_data['class_name'] == class_name) & (erg_data['gender'] == gender)] == 0) | (erg_data[(erg_data['class_name'] == class_name) & (erg_data['gender'] == gender)] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif ((section != 'all') & (class_name != 'all') & (gender == 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section)] == 0) | (dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section)] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section)] == 0) | (ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section)] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section)] == 0) | (vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section)] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section)] == 0) | (hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section)] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section)] == 0) | (phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section)] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section)] == 0) | (eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section)] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[(erg_data['class_name'] == class_name) & (erg_data['section'] == section)] == 0) | (erg_data[(erg_data['class_name'] == class_name) & (erg_data['section'] == section)] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif (class_name == 'all') & (section == 'all') & (gender != 'all'):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[dent_data['gender'] == gender] == 0) | (dent_data[dent_data['gender'] == gender] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[ent_data['gender'] == gender] == 0) | (ent_data[ent_data['gender'] == gender] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[vit_data['gender'] == gender] == 0) | (vit_data[vit_data['gender'] == gender] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[hyg_data['gender'] == gender] == 0) | (hyg_data[hyg_data['gender'] == gender] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[phy_data['gender'] == gender] == 0) | (phy_data[phy_data['gender'] == gender] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[eye_data['gender'] == gender] == 0) | (eye_data[eye_data['gender'] == gender] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[erg_data['gender'] == gender] == 0) | (erg_data[erg_data['gender'] == gender] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif (class_name == 'all') & (gender == 'all') & (section != 'all'):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[dent_data['section'] == section] == 0) | (dent_data[dent_data['section'] == section] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[ent_data['section'] == section] == 0) | (ent_data[ent_data['section'] == section] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[vit_data['section'] == section] == 0) | (vit_data[vit_data['section'] == section] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[hyg_data['section'] == section] == 0) | (hyg_data[hyg_data['section'] == section] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[phy_data['section'] == section] == 0) | (phy_data[phy_data['section'] == section] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[eye_data['section'] == section] == 0) | (eye_data[eye_data['section'] == section] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[erg_data['section'] == section] == 0) | (erg_data[erg_data['section'] == section] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif (section == 'all') & (gender == 'all') & (class_name != 'all'):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[dent_data['class_name'] == class_name] == 0) | (dent_data[dent_data['class_name'] == class_name] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[ent_data['class_name'] == class_name] == 0) | (ent_data[ent_data['class_name'] == class_name] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[vit_data['class_name'] == class_name] == 0) | (vit_data[vit_data['class_name'] == class_name] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[hyg_data['class_name'] == class_name] == 0) | (hyg_data[hyg_data['class_name'] == class_name] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[phy_data['class_name'] == class_name] == 0) | (phy_data[phy_data['class_name'] == class_name] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[eye_data['class_name'] == class_name] == 0) | (eye_data[eye_data['class_name'] == class_name] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[erg_data['class_name']  == class_name] == 0) | (erg_data[erg_data['class_name'] == class_name] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif ((class_name == 'all') & (section == 'all') & (gender == 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data == 0) | (dent_data == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data == 0) | (ent_data == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data == 0) | (vit_data == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data == 0) | (hyg_data == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data == 0) | (phy_data == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data == 0) | (eye_data == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data == 0) | (erg_data == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        else:
            d_var = dent_data[(dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section) & (
                        dent_data['gender'] == gender)] == 0) |
                           (dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section) & (
                                       dent_data['gender'] == gender)] == 0.5)].count(axis=1)
            e_var = ent_data[(ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section) & (
                        ent_data['gender'] == gender)] == 0) |
                           (ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section) & (
                                       ent_data['gender'] == gender)] == 0.5)].count(axis=1)
            v_var = vit_data[(vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section) & (
                        vit_data['gender'] == gender)] == 0) |
                           (vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section) & (
                                       vit_data['gender'] == gender)] == 0.5)].count(axis=1)
            h_var = hyg_data[(hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section) & (
                        hyg_data['gender'] == gender)] == 0) |
                           (hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section) & (
                                       hyg_data['gender'] == gender)] == 0.5)].count(axis=1)
            p_var = phy_data[(phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section) & (
                        phy_data['gender'] == gender)] == 0) |
                           (phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section) & (
                                       phy_data['gender'] == gender)] == 0.5)].count(axis=1)
            eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section) & (
                        eye_data['gender'] == gender)] == 0) |
                               (eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section) & (
                                           eye_data['gender'] == gender)] == 0.5)].count(axis=1)
            ergo_var = erg_data[(erg_data[
                                      (erg_data['class_name'] == class_name) & (erg_data['section'] == section) & (
                                                  erg_data['gender'] == gender)] == 0) |
                                 (erg_data[
                                      (erg_data['class_name'] == class_name) & (erg_data['section'] == section) & (
                                                  erg_data['gender'] == gender)] == 0.5)].count(axis=1)

        dic = {
            'dental':
                {
                    # 'dent_atleast1':dent_atleast1,
                    'Bleeding': list(d_var)[0],
                    'Impaction': list(d_var)[1],
                    'Inflamation': list(d_var)[2],
                    'Teethcondition': list(d_var)[3],
                    'Gum Vitality': list(d_var)[4],
                    'Alignment': list(d_var)[5],
                    'Badbreath': list(d_var)[6],
                    'Cavities': list(d_var)[7],
                    'Plaque': list(d_var)[8],
                    'Tarter': list(d_var)[9],
                    'Strains': list(d_var)[10],
                    'Dental Vitality': list(d_var)[11]
                },
            'vitals':
                {
                    # 'vit_atleast1' : vit_atleast1
                    'BMI': list(v_var)[0],
                    'BP (Systolic)': list(v_var)[1],
                    'BP (Diastolic)': list(v_var)[2],
                    'Height': list(v_var)[3],
                    'Oxygensaturation': list(v_var)[4],
                    'Pulserate': list(v_var)[5],
                    'Respiratoryrate': list(v_var)[6],
                    'Spirometer': list(v_var)[7],
                    'Temperature': list(v_var)[8],
                    'Weight': list(v_var)[9]
                },
            'eye':
                {
                    # 'eye_atleast1' :eye_atleast1,
                    'AbnormalEyeMovement': list(eye_var)[0],
                    'Anisocoria': list(eye_var)[1],
                    'Anisometropia': list(eye_var)[2],
                    'Astigmatism': list(eye_var)[3],
                    'Bitotspots': list(eye_var)[4],
                    'Cornealscar': list(eye_var)[5],
                    'Gazeasymmetry': list(eye_var)[6],
                    'Hyperopia': list(eye_var)[7],
                    'Myopia': list(eye_var)[8],
                    'Squint': list(eye_var)[9],
                    'VisionScreeningResult': list(eye_var)[10],
                    'Wearglass': list(eye_var)[11]
                },
            'ergonomics':
                {
                    # 'erg_atleast1; : erg_no,
                    'JointMovements': list(ergo_var)[0],
                    'MuscleStrength': list(ergo_var)[1],
                    'OverallBone': list(ergo_var)[2]
                },
            'hygiene':
                {
                    # "hyg_atleast1' : hyg_no,
                    'HairColour': list(h_var)[0],
                    'HairCondition': list(h_var)[1],
                    'HairDandruff': list(h_var)[2],
                    'HairLice': list(h_var)[3],
                    'Nails': list(h_var)[4],
                    'SkinCondition': list(h_var)[5],
                    'SkinRash': list(h_var)[6]
                },
            'physical':
                {
                    # 'phy_atleast1': phy_no,
                    'Abdomen': list(p_var)[0],
                    'Back': list(p_var)[1],
                    'Chest': list(p_var)[2],
                    'Clubbing': list(p_var)[3],
                    'Cyanosis': list(p_var)[4],
                    'Edema': list(p_var)[5],
                    'AbnormalFingers': list(p_var)[6],
                    'ExtraFingers': list(p_var)[7],
                    'FusedFingers': list(p_var)[8],
                    'Icterus': list(p_var)[9],
                    'Koilonychia': list(p_var)[10],
                    'Lowershape': list(p_var)[11],
                    'LowerSwellingOfJoints': list(p_var)[12],
                    'Lymphadenopathy': list(p_var)[13],
                    'Pallor': list(p_var)[14],
                    'Thyroid': list(p_var)[15],
                    'AbnormalToes': list(p_var)[16],
                    'ExtraToes': list(p_var)[17],
                    'FusedToes': list(p_var)[18],
                    'UpperShape': list(p_var)[19],
                    'UpperSwellingOfJoint': list(p_var)[20],
                    'Abdominaldistention': list(p_var)[21],
                    'Hernia': list(p_var)[22],
                    'Liver': list(p_var)[23],
                    'Mass': list(p_var)[24],
                    'Scars': list(p_var)[25],
                    'Spleen': list(p_var)[26],
                    'VisibleBloodVessels': list(p_var)[27],
                    'Cardiores': list(p_var)[28],
                    'Murmur': list(p_var)[29],
                    'CranialNerves': list(p_var)[30],
                    'MentalStatusTesting': list(p_var)[31],
                    'Power': list(p_var)[32],
                    'Reflexes': list(p_var)[33],
                    'Sensation': list(p_var)[34],
                    'Tone': list(p_var)[35],
                    'Respres': list(p_var)[36],
                    'Breathres': list(p_var)[37]
                },
            'ent':
                {
                    # 'ent_atlest1' : ent_atleast1,
                    'LeftDischarge': list(e_var)[0],
                    'LeftHygiene': list(e_var)[1],
                    'LeftPerforation': list(e_var)[2],
                    'LeftPinna': list(e_var)[3],
                    'LeftPit': list(e_var)[4],
                    'LeftWaxImpacted': list(e_var)[5],
                    'RightDischarge': list(e_var)[6],
                    'RightHygiene': list(e_var)[7],
                    'RightPerforation': list(e_var)[8],
                    'RightPinnacolor': list(e_var)[9],
                    'RightPitcolor': list(e_var)[10],
                    'RightWaxImpacted': list(e_var)[11],
                    'LeftHypertrophideturbinate': list(e_var)[12],
                    'RightHypertrophideturbinate': list(e_var)[13],
                    'Thrush': list(e_var)[14],
                    'Tongueglossitis': list(e_var)[15],
                    'Tonguetie': list(e_var)[16],
                    'Tonsils': list(e_var)[17]
                },
        }
    else:
        df = df[df['branch_id'] == sel_branch]
        vit_cols = []
        for k in df.columns:
            if ((k.find("generic") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                vit_cols.append(k)
        vital_fields_new = ['BMI', 'BP (Systolic)', 'BP (Diastolic)', 'Height',
                            'Oxygensaturation',
                            'Pulserate', 'Respiratoryrate', 'Spirometer', 'Temperature', 'Weight', 'class_name',
                            'section', 'gender']
        vit_data = df[vit_cols]
        vit_data.columns = vital_fields_new
        # vit_no = df[vit_cols][(df[vit_cols] == '0') | (df[vit_cols] == '0.5')].count(axis=1)
        # vit_atleast1 = vit_no[vit_no >= 1].count()
        phy_cols = []
        for k in df.columns:
            if ((k.find("pickle") == 0) | (k.find("sysexam") == 0) | (k.find("gender") == 0) | (
                    k.find("class_name") == 0) | (k.find("section") == 0)):
                phy_cols.append(k)
        phy_fields_new = ['Abdomen', 'Back', 'Chest', 'Clubbing', 'Cyanosis', 'Edema',
                          'AbnormalFingers', 'ExtraFingers', 'FusedFingers', 'Icterus', 'Koilonychia', 'Lowershape',
                          'LowerSwellingOfJoints', 'Lymphadenopathy', 'Pallor', 'Thyroid', 'AbnormalToes', 'ExtraToes',
                          'FusedToes', 'UpperShape', 'UpperSwellingOfJoint', 'Abdominaldistention', 'Hernia',
                          'Liver', 'Mass', 'Scars', 'Spleen', 'VisibleBloodVessels', 'Cardiores', 'Murmur',
                          'CranialNerves', 'MentalStatusTesting', 'Power', 'Reflexes', 'Sensation', 'Tone', 'Respres',
                          'Breathres', 'class_name', 'section', 'gender']
        phy_data = df[phy_cols]
        phy_data.columns = phy_fields_new
        ergonomics_cols = []
        for k in df.columns:
            if ((k.find("ergonomics_") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                ergonomics_cols.append(k)
        ergonomics_fields_new = ['JointMovements', 'MuscleStrength', 'OverallBone', 'class_name', 'section', 'gender']
        erg_data = df[ergonomics_cols]
        erg_data.columns = ergonomics_fields_new
        hyg_cols = []
        for k in df.columns:
            if ((k.find("hygiene") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                hyg_cols.append(k)
        hyg_fields_new = ['HairColour', 'HairCondition', 'HairDandruff', 'HairLice', 'Nails', 'SkinCondition',
                          'SkinRash', 'class_name', 'section', 'gender']
        hyg_data = df[hyg_cols]
        hyg_data.columns = hyg_fields_new

        # phy_no = df[phy_cols][(df[phy_cols] == '0') | (df[phy_cols] == '0.5')].count(axis=1)
        # erg_no = df[ergonomics_cols][(df[ergonomics_cols] == '0') | (df[ergonomics_cols] == '0.5')].count(axis=1)
        # hyg_no = df[hyg_cols][(df[hyg_cols] == '0') | (df[hyg_cols] == '0.5')].count(axis=1)
        # phy_atl = phy_no[phy_no >= 1].index
        # erg_atl = erg_no[erg_no >= 1].index
        # hyg_atl = hyg_no[hyg_no >= 1].index
        # phy_final = list(set(phy_atl) | set(hyg_atl) | set(erg_atl))
        # phy_final = set(phy_final)
        # phy_atleast1 = len(phy_final)

        dent_cols = []
        for k in df.columns:
            if ((k.find("dental") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                dent_cols.append(k)
        dental_fields_new = ['Bleeding', 'Impaction', 'Inflamation', 'Teethcondition', 'Gum Vitality', 'Alignment',
                             'Badbreath', 'Cavities', 'Plaque', 'Strains', 'Tarter', 'Dental Vitality', 'class_name',
                             'gender', 'section']
        dent_data = df[dent_cols]
        dent_data.columns = dental_fields_new
        # dent_no = df[dent_cols][(df[dent_cols] == '0') | (df[dent_cols] == '0.5')].count(axis=1)
        # dent_atleast1 = dent_no[dent_no >= 1].count()
        ent_cols = []
        for k in df.columns:
            if ((k.find("ent_") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                ent_cols.append(k)
        ent_fields_new = ['LeftDischarge', 'LeftHygiene', 'LeftPerforation', 'LeftPinna', 'LeftPit',
                          'LeftWaxImpacted', 'RightDischarge', 'RightHygiene', 'RightPerforation', 'RightPinnacolor',
                          'RightPitcolor', 'RightWaxImpacted', 'LeftHypertrophideturbinate',
                          'RightHypertrophideturbinate', 'Thrush', 'Tongueglossitis', 'Tonguetie', 'Tonsils',
                          'class_name', 'section', 'gender']
        ent_data = df[ent_cols]
        ent_data.columns = ent_fields_new
        # ent_no = df[ent_cols][(df[ent_cols] == '0') | (df[ent_cols] == '0.5')].count(axis=1)
        # ent_atleast1 = ent_no[ent_no >= 1].count()
        eye_cols = []
        for k in df.columns:
            if ((k.find("eyes") == 0) | (k.find("gender") == 0) | (k.find("class_name") == 0) | (
                    k.find("section") == 0)):
                eye_cols.append(k)
        eye_fields_new = ['AbnormalEyeMovement', 'Anisocoria', 'Anisometropia', 'Astigmatism',
                          'Bitotspots',
                          'Cornealscar', 'Gazeasymmetry', 'Hyperopia', 'Myopia', 'Squint', 'VisionScreeningResult',
                          'Wearglass', 'class_name', 'section', 'gender']
        eye_data = df[eye_cols]
        eye_data.columns = eye_fields_new
        # eye_no = df[eye_cols][(df[eye_cols] == '0') | (df[eye_cols] == '0.5')].count(axis=1)
        # eye_atleast1 = eye_no[eye_no >= 1].count()

        if ((class_name == 'all') & (section != 'all') & (gender != 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[(dent_data['section'] == section) & (dent_data['gender'] == gender)] == 0) | (
                        dent_data[(dent_data['section'] == section) & (dent_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            e_var = ent_data[(ent_data[(ent_data['section'] == section) & (ent_data['gender'] == gender)] == 0) | (
                        ent_data[(ent_data['section'] == section) & (ent_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            v_var = vit_data[(vit_data[(vit_data['section'] == section) & (vit_data['gender'] == gender)] == 0) | (
                        vit_data[(vit_data['section'] == section) & (vit_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            h_var = hyg_data[(hyg_data[(hyg_data['section'] == section) & (hyg_data['gender'] == gender)] == 0) | (
                        hyg_data[(hyg_data['section'] == section) & (hyg_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            p_var = phy_data[(phy_data[(phy_data['section'] == section) & (phy_data['gender'] == gender)] == 0) | (
                        phy_data[(phy_data['section'] == section) & (phy_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            eye_var = eye_data[(eye_data[(eye_data['section'] == section) & (eye_data['gender'] == gender)] == 0) | (
                        eye_data[(eye_data['section'] == section) & (eye_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            ergo_var = erg_data[(erg_data[(erg_data['section'] == section) & (erg_data['gender'] == gender)] == 0) | (
                        erg_data[(erg_data['section'] == section) & (erg_data['gender'] == gender)] == 0.5)].count(
                axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)


        elif ((section == 'all') & (class_name != 'all') & (gender != 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[
                (dent_data[(dent_data['class_name'] == class_name) & (dent_data['gender'] == gender)] == 0) | (
                            dent_data[(dent_data['class_name'] == class_name) & (
                                        dent_data['gender'] == gender)] == 0.5)].count(axis=0)
            e_var = ent_data[
                (ent_data[(ent_data['class_name'] == class_name) & (ent_data['gender'] == gender)] == 0) | (ent_data[(
                                                                                                                                 ent_data[
                                                                                                                                     'class_name'] == class_name) & (
                                                                                                                                 ent_data[
                                                                                                                                     'gender'] == gender)] == 0.5)].count(
                axis=0)
            v_var = vit_data[
                (vit_data[(vit_data['class_name'] == class_name) & (vit_data['gender'] == gender)] == 0) | (vit_data[(
                                                                                                                                 vit_data[
                                                                                                                                     'class_name'] == class_name) & (
                                                                                                                                 vit_data[
                                                                                                                                     'gender'] == gender)] == 0.5)].count(
                axis=0)
            h_var = hyg_data[
                (hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['gender'] == gender)] == 0) | (hyg_data[(
                                                                                                                                 hyg_data[
                                                                                                                                     'class_name'] == class_name) & (
                                                                                                                                 hyg_data[
                                                                                                                                     'gender'] == gender)] == 0.5)].count(
                axis=0)
            p_var = phy_data[
                (phy_data[(phy_data['class_name'] == class_name) & (phy_data['gender'] == gender)] == 0) | (phy_data[(
                                                                                                                                 phy_data[
                                                                                                                                     'class_name'] == class_name) & (
                                                                                                                                 phy_data[
                                                                                                                                     'gender'] == gender)] == 0.5)].count(
                axis=0)
            eye_var = eye_data[
                (eye_data[(eye_data['class_name'] == class_name) & (eye_data['gender'] == gender)] == 0) | (eye_data[(
                                                                                                                                 eye_data[
                                                                                                                                     'class_name'] == class_name) & (
                                                                                                                                 eye_data[
                                                                                                                                     'gender'] == gender)] == 0.5)].count(
                axis=0)
            ergo_var = erg_data[
                (erg_data[(erg_data['class_name'] == class_name) & (erg_data['gender'] == gender)] == 0) | (erg_data[(
                                                                                                                                 erg_data[
                                                                                                                                     'class_name'] == class_name) & (
                                                                                                                                 erg_data[
                                                                                                                                     'gender'] == gender)] == 0.5)].count(
                axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif ((section != 'all') & (class_name != 'all') & (gender == 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[
                (dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section)] == 0) | (
                            dent_data[(dent_data['class_name'] == class_name) & (
                                        dent_data['section'] == section)] == 0.5)].count(axis=0)
            e_var = ent_data[
                (ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section)] == 0) | (ent_data[(
                                                                                                                                   ent_data[
                                                                                                                                       'class_name'] == class_name) & (
                                                                                                                                   ent_data[
                                                                                                                                       'section'] == section)] == 0.5)].count(
                axis=0)
            v_var = vit_data[
                (vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section)] == 0) | (vit_data[(
                                                                                                                                   vit_data[
                                                                                                                                       'class_name'] == class_name) & (
                                                                                                                                   vit_data[
                                                                                                                                       'section'] == section)] == 0.5)].count(
                axis=0)
            h_var = hyg_data[
                (hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section)] == 0) | (hyg_data[(
                                                                                                                                   hyg_data[
                                                                                                                                       'class_name'] == class_name) & (
                                                                                                                                   hyg_data[
                                                                                                                                       'section'] == section)] == 0.5)].count(
                axis=0)
            p_var = phy_data[
                (phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section)] == 0) | (phy_data[(
                                                                                                                                   phy_data[
                                                                                                                                       'class_name'] == class_name) & (
                                                                                                                                   phy_data[
                                                                                                                                       'section'] == section)] == 0.5)].count(
                axis=0)
            eye_var = eye_data[
                (eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section)] == 0) | (eye_data[(
                                                                                                                                   eye_data[
                                                                                                                                       'class_name'] == class_name) & (
                                                                                                                                   eye_data[
                                                                                                                                       'section'] == section)] == 0.5)].count(
                axis=0)
            ergo_var = erg_data[
                (erg_data[(erg_data['class_name'] == class_name) & (erg_data['section'] == section)] == 0) | (erg_data[(
                                                                                                                                   erg_data[
                                                                                                                                       'class_name'] == class_name) & (
                                                                                                                                   erg_data[
                                                                                                                                       'section'] == section)] == 0.5)].count(
                axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif (class_name == 'all') & (section == 'all') & (gender != 'all'):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[dent_data['gender'] == gender] == 0) | (
                        dent_data[dent_data['gender'] == gender] == 0.5)].count(axis=0)
            e_var = ent_data[
                (ent_data[ent_data['gender'] == gender] == 0) | (ent_data[ent_data['gender'] == gender] == 0.5)].count(
                axis=0)
            v_var = vit_data[
                (vit_data[vit_data['gender'] == gender] == 0) | (vit_data[vit_data['gender'] == gender] == 0.5)].count(
                axis=0)
            h_var = hyg_data[
                (hyg_data[hyg_data['gender'] == gender] == 0) | (hyg_data[hyg_data['gender'] == gender] == 0.5)].count(
                axis=0)
            p_var = phy_data[
                (phy_data[phy_data['gender'] == gender] == 0) | (phy_data[phy_data['gender'] == gender] == 0.5)].count(
                axis=0)
            eye_var = eye_data[
                (eye_data[eye_data['gender'] == gender] == 0) | (eye_data[eye_data['gender'] == gender] == 0.5)].count(
                axis=0)
            ergo_var = erg_data[
                (erg_data[erg_data['gender'] == gender] == 0) | (erg_data[erg_data['gender'] == gender] == 0.5)].count(
                axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif (class_name == 'all') & (gender == 'all') & (section != 'all'):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[dent_data['section'] == section] == 0) | (
                        dent_data[dent_data['section'] == section] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[ent_data['section'] == section] == 0) | (
                        ent_data[ent_data['section'] == section] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[vit_data['section'] == section] == 0) | (
                        vit_data[vit_data['section'] == section] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[hyg_data['section'] == section] == 0) | (
                        hyg_data[hyg_data['section'] == section] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[phy_data['section'] == section] == 0) | (
                        phy_data[phy_data['section'] == section] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[eye_data['section'] == section] == 0) | (
                        eye_data[eye_data['section'] == section] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[erg_data['section'] == section] == 0) | (
                        erg_data[erg_data['section'] == section] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif (section == 'all') & (gender == 'all') & (class_name != 'all'):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data[dent_data['class_name'] == class_name] == 0) | (
                        dent_data[dent_data['class_name'] == class_name] == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data[ent_data['class_name'] == class_name] == 0) | (
                        ent_data[ent_data['class_name'] == class_name] == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data[vit_data['class_name'] == class_name] == 0) | (
                        vit_data[vit_data['class_name'] == class_name] == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data[hyg_data['class_name'] == class_name] == 0) | (
                        hyg_data[hyg_data['class_name'] == class_name] == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data[phy_data['class_name'] == class_name] == 0) | (
                        phy_data[phy_data['class_name'] == class_name] == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data[eye_data['class_name'] == class_name] == 0) | (
                        eye_data[eye_data['class_name'] == class_name] == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data[erg_data['class_name'] == class_name] == 0) | (
                        erg_data[erg_data['class_name'] == class_name] == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        elif ((class_name == 'all') & (section == 'all') & (gender == 'all')):
            total = dent_data.shape[0]
            d_var = dent_data[(dent_data == 0) | (dent_data == 0.5)].count(axis=0)
            e_var = ent_data[(ent_data == 0) | (ent_data == 0.5)].count(axis=0)
            v_var = vit_data[(vit_data == 0) | (vit_data == 0.5)].count(axis=0)
            h_var = hyg_data[(hyg_data == 0) | (hyg_data == 0.5)].count(axis=0)
            p_var = phy_data[(phy_data == 0) | (phy_data == 0.5)].count(axis=0)
            eye_var = eye_data[(eye_data == 0) | (eye_data == 0.5)].count(axis=0)
            ergo_var = erg_data[(erg_data == 0) | (erg_data == 0.5)].count(axis=0)
            d_var = round(d_var / total * 100, 2)
            e_var = round(e_var / total * 100, 2)
            v_var = round(v_var / total * 100, 2)
            h_var = round(h_var / total * 100, 2)
            p_var = round(p_var / total * 100, 2)
            eye_var = round(eye_var / total * 100, 2)
            ergo_var = round(ergo_var / total * 100, 2)

        else:
            d_var = dent_data[(dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section) & (
                        dent_data['gender'] == gender)] == 0) |
                           (dent_data[(dent_data['class_name'] == class_name) & (dent_data['section'] == section) & (
                                       dent_data['gender'] == gender)] == 0.5)].count(axis=1)
            e_var = ent_data[(ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section) & (
                        ent_data['gender'] == gender)] == 0) |
                           (ent_data[(ent_data['class_name'] == class_name) & (ent_data['section'] == section) & (
                                       ent_data['gender'] == gender)] == 0.5)].count(axis=1)
            v_var = vit_data[(vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section) & (
                        vit_data['gender'] == gender)] == 0) |
                           (vit_data[(vit_data['class_name'] == class_name) & (vit_data['section'] == section) & (
                                       vit_data['gender'] == gender)] == 0.5)].count(axis=1)
            h_var = hyg_data[(hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section) & (
                        hyg_data['gender'] == gender)] == 0) |
                           (hyg_data[(hyg_data['class_name'] == class_name) & (hyg_data['section'] == section) & (
                                       hyg_data['gender'] == gender)] == 0.5)].count(axis=1)
            p_var = phy_data[(phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section) & (
                        phy_data['gender'] == gender)] == 0) |
                           (phy_data[(phy_data['class_name'] == class_name) & (phy_data['section'] == section) & (
                                       phy_data['gender'] == gender)] == 0.5)].count(axis=1)
            eye_var = eye_data[(eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section) & (
                        eye_data['gender'] == gender)] == 0) |
                               (eye_data[(eye_data['class_name'] == class_name) & (eye_data['section'] == section) & (
                                           eye_data['gender'] == gender)] == 0.5)].count(axis=1)
            ergo_var = erg_data[(erg_data[
                                      (erg_data['class_name'] == class_name) & (erg_data['section'] == section) & (
                                                  erg_data['gender'] == gender)] == 0) |
                                 (erg_data[
                                      (erg_data['class_name'] == class_name) & (erg_data['section'] == section) & (
                                                  erg_data['gender'] == gender)] == 0.5)].count(axis=1)

        dic = {
            'dental':
                {
                    # 'dent_atleast1':dent_atleast1,
                    'Bleeding': list(d_var)[0],
                    'Impaction': list(d_var)[1],
                    'Inflamation': list(d_var)[2],
                    'Teethcondition': list(d_var)[3],
                    'Gum Vitality': list(d_var)[4],
                    'Alignment': list(d_var)[5],
                    'Badbreath': list(d_var)[6],
                    'Cavities': list(d_var)[7],
                    'Plaque': list(d_var)[8],
                    'Tarter': list(d_var)[9],
                    'Strains': list(d_var)[10],
                    'Dental Vitality': list(d_var)[11]
                },
            'vitals':
                {
                    # 'vit_atleast1' : vit_atleast1
                    'BMI': list(v_var)[0],
                    'BP (Systolic)': list(v_var)[1],
                    'BP (Diastolic)': list(v_var)[2],
                    'Height': list(v_var)[3],
                    'Oxygensaturation': list(v_var)[4],
                    'Pulserate': list(v_var)[5],
                    'Respiratoryrate': list(v_var)[6],
                    'Spirometer': list(v_var)[7],
                    'Temperature': list(v_var)[8],
                    'Weight': list(v_var)[9]
                },
            'eye':
                {
                    # 'eye_atleast1' :eye_atleast1,
                    'AbnormalEyeMovement': list(eye_var)[0],
                    'Anisocoria': list(eye_var)[1],
                    'Anisometropia': list(eye_var)[2],
                    'Astigmatism': list(eye_var)[3],
                    'Bitotspots': list(eye_var)[4],
                    'Cornealscar': list(eye_var)[5],
                    'Gazeasymmetry': list(eye_var)[6],
                    'Hyperopia': list(eye_var)[7],
                    'Myopia': list(eye_var)[8],
                    'Squint': list(eye_var)[9],
                    'VisionScreeningResult': list(eye_var)[10],
                    'Wearglass': list(eye_var)[11]
                },
            'ergonomics':
                {
                    # 'erg_atleast1; : erg_no,
                    'JointMovements': list(ergo_var)[0],
                    'MuscleStrength': list(ergo_var)[1],
                    'OverallBone': list(ergo_var)[2]
                },
            'hygiene':
                {
                    # "hyg_atleast1' : hyg_no,
                    'HairColour': list(h_var)[0],
                    'HairCondition': list(h_var)[1],
                    'HairDandruff': list(h_var)[2],
                    'HairLice': list(h_var)[3],
                    'Nails': list(h_var)[4],
                    'SkinCondition': list(h_var)[5],
                    'SkinRash': list(h_var)[6]
                },
            'physical':
                {
                    # 'phy_atleast1': phy_no,
                    'Abdomen': list(p_var)[0],
                    'Back': list(p_var)[1],
                    'Chest': list(p_var)[2],
                    'Clubbing': list(p_var)[3],
                    'Cyanosis': list(p_var)[4],
                    'Edema': list(p_var)[5],
                    'AbnormalFingers': list(p_var)[6],
                    'ExtraFingers': list(p_var)[7],
                    'FusedFingers': list(p_var)[8],
                    'Icterus': list(p_var)[9],
                    'Koilonychia': list(p_var)[10],
                    'Lowershape': list(p_var)[11],
                    'LowerSwellingOfJoints': list(p_var)[12],
                    'Lymphadenopathy': list(p_var)[13],
                    'Pallor': list(p_var)[14],
                    'Thyroid': list(p_var)[15],
                    'AbnormalToes': list(p_var)[16],
                    'ExtraToes': list(p_var)[17],
                    'FusedToes': list(p_var)[18],
                    'UpperShape': list(p_var)[19],
                    'UpperSwellingOfJoint': list(p_var)[20],
                    'Abdominaldistention': list(p_var)[21],
                    'Hernia': list(p_var)[22],
                    'Liver': list(p_var)[23],
                    'Mass': list(p_var)[24],
                    'Scars': list(p_var)[25],
                    'Spleen': list(p_var)[26],
                    'VisibleBloodVessels': list(p_var)[27],
                    'Cardiores': list(p_var)[28],
                    'Murmur': list(p_var)[29],
                    'CranialNerves': list(p_var)[30],
                    'MentalStatusTesting': list(p_var)[31],
                    'Power': list(p_var)[32],
                    'Reflexes': list(p_var)[33],
                    'Sensation': list(p_var)[34],
                    'Tone': list(p_var)[35],
                    'Respres': list(p_var)[36],
                    'Breathres': list(p_var)[37]
                },
            'ent':
                {
                    # 'ent_atlest1' : ent_atleast1,
                    'LeftDischarge': list(e_var)[0],
                    'LeftHygiene': list(e_var)[1],
                    'LeftPerforation': list(e_var)[2],
                    'LeftPinna': list(e_var)[3],
                    'LeftPit': list(e_var)[4],
                    'LeftWaxImpacted': list(e_var)[5],
                    'RightDischarge': list(e_var)[6],
                    'RightHygiene': list(e_var)[7],
                    'RightPerforation': list(e_var)[8],
                    'RightPinnacolor': list(e_var)[9],
                    'RightPitcolor': list(e_var)[10],
                    'RightWaxImpacted': list(e_var)[11],
                    'LeftHypertrophideturbinate': list(e_var)[12],
                    'RightHypertrophideturbinate': list(e_var)[13],
                    'Thrush': list(e_var)[14],
                    'Tongueglossitis': list(e_var)[15],
                    'Tonguetie': list(e_var)[16],
                    'Tonsils': list(e_var)[17]
                },
        }
    return (dic)

def pop(x):
    import pandas as pd
    import numpy as np

    df = pd.read_csv("branch_Wise.csv", keep_default_na=False)
    df = df[df.generic_tempcolor != 'null']
    df.replace(' ', np.nan, inplace=True)
    df.replace('', np.nan, inplace=True)
    df.replace('null', np.nan, inplace=True)
    df = df[df['branch_id'] == x]

    uni_gender = list(df['gender'].dropna().unique())
    uni_class = list(df['class_name'].dropna().unique())
    uni_section = list(df['section'].dropna().unique())
    var ='all'
    uni_gender.insert(0, var)
    uni_class.insert(0, var)
    uni_section.insert(0, var)
    print(uni_section)
    dic={
        'class': uni_class,
        'gender': uni_gender,
        'section': uni_section
    }

    return (dic)
