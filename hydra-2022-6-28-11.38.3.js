// licensed with CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/
s0.initScreen()
src(o3).scrollY(()=>(time/-10)).mult(src(o1).diff(o2)).diff(o0).out()
osc(1,2,300).diff(gradient(1)).scale(.1).invert().out(o1)
src(s0).out(o2)
shape(2,.1).out(o3)
render(o0)
