import webcamPreprocess

contours,Img_shape = webcamPreprocess.preProcess()
x_scaler = Img_shape[1] / 150
y_scaler = Img_shape[0] / 150
scaler = max(x_scaler, y_scaler)
left_x = 0
left_y = 0
gcode = "G00 X0 Y0\n"
gcode = gcode + f"M03 S250 \n"
j=0
for contour in contours:
    i = 1
    gcode = gcode + f"G00 X{contours[j][0][0][0] / scaler + left_x} Y{contours[j][0][0][1] / scaler + left_y};\n"
    # print(len(contour))
    gcode = gcode + f"M03 S0 \n"
    gcode = gcode + f"G04 P1\n"
    while i < len(contour):
        x = contour[i][0][0] / scaler
        y = contour[i][0][1] / scaler
        code = f"G00  X{x + left_x} Y{y + left_y};\n"
        gcode = gcode + code
        i = i + 1
    gcode = gcode + f"M03 S250 \n"
    gcode = gcode + f"G04 P1 \n"
    if j<=len(contours):
        j=j+1
gcode = gcode + f"G00 X0 Y0 \n"
gcode = gcode + f"M03 S250 \n"
print(gcode)
path = r'C:....\gcode.nc' #replace file location
f = open('gcode.nc', 'w')
f.write(gcode)
