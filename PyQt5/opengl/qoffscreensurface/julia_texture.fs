#version 430 core

uniform sampler1D sampler;
uniform vec2 c;
uniform int iter;

in VS_OUT
{
	vec2 texc;
} fs_in;

out vec4 color;

void main(void)
{
    vec2 z;
    z.x = 3.0 * (fs_in.texc.x - 0.5);
    z.y = 2.0 * (fs_in.texc.y - 0.5);

    int i;
    for(i=0; i<iter; i++) {
            float x = (z.x * z.x - z.y * z.y) + c.x;
            float y = (z.y * z.x + z.x * z.y) + c.y;

            if((x * x + y * y) > 4.0) break;
            z.x = x;
            z.y = y;
    }

    color = texture(sampler, (i == iter ? 0.0 : float(i)) / 100.0);
}
