#version 430 core

in VS_OUT
{
	vec4 col;
} fs_in;

out vec4 color;

void main(void)
{
    color = fs_in.col;
}