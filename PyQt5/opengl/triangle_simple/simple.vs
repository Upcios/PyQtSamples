#version 430 core

in vec3 position;
in vec4 color;

uniform mat4 mvp;

out VS_OUT
{
	vec4 col;
} vs_out;

void main(void)
{
    vs_out.col = color;
    gl_Position = mvp * vec4(position, 1.0);
}