// licensed with CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/
//
s0.initVideo("https://upload.wikimedia.org/wikipedia/commons/a/a7/Jumping_jack_movimiento.ogg")
src(s0).invert().colorama(.4).modulate(src(s0).add(s0).thresh(),.07).diff(src(o0).pixelate().diff(src(o0).scale(.50).diff(src(o0).scale(1.15).luma(.75).hue().saturate([1.9,.99,1.01,1.1].smooth(1/4).fast(1/4)).brightness(-.5)))).out()
