Write a function that returns the total surface area and volume of a box as an array: [area, volume]

def get_size(w,h,d):
    volume = w * h * d
    surface_area = 2*w*h + 2*h*d + 2*w*d
    return [surface_area,volume]
