#version 430 core

uniform sampler2D texture;

in VS_OUT
{
	vec2 texc;
} fs_in;

out vec4 color;

void main(void)
{
    color = texture2D(texture, fs_in.texc);
}