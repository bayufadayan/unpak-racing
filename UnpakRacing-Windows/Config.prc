load-display pandagl
aux-display pandadx9
aux-display p3tinydisplay

plugin-path $THIS_PRC_DIR
plugin-path $THIS_PRC_DIR/_internal/panda3d

model-path $MAIN_DIR
model-path $THIS_PRC_DIR

win-origin -2 -2
win-size 800 600
fullscreen #f
framebuffer-hardware #t
framebuffer-software #f
depth-bits 1
color-bits 1 1 1
alpha-bits 0
stencil-bits 0
multisamples 0
notify-level warning
default-directnotify-level warning
audio-library-name p3openal_audio
use-movietexture #t
hardware-animated-vertices #f
model-cache-dir $USER_APPDATA/Panda3D-1.10
model-cache-textures #f
basic-shaders-only #f
