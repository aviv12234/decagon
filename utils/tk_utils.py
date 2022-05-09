

def animation(window, count, gif_label, num_frames, photo_list):
    im2 = photo_list[count]

    gif_label.configure(image=im2)
    count += 2
    if count == num_frames:
        count = 0
    window.after(50,lambda :animation(count))