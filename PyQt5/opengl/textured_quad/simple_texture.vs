#version 430 core

in vec3 position;
in vec2 texCoord;

uniform mat4 mvp;

out VS_OUT
{
	vec2 texc;
} vs_out;

void main(void)
{
    gl_Position = mvp * vec4(position, 1.0);
    vs_out.texc = texCoord;
}