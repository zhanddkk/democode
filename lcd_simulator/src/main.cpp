/*
 * main.cpp
 *
 *  Created on: Sep 4, 2018
 *      Author: zhanlei
 */

/*
 * need those libraries
 * sudo apt-get install build-essential
 * sudo apt-get install libgl1-mesa-dev
 * sudo apt-get install libglu1-mesa-dev
 * sudo apt-get install freeglut3-dev
 */

#include <GL/glut.h>

void draw()
{
	glViewport(0, 0, 600, 300);
    glClearColor(0, 0, 1, 1);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0f, 1.0f, 0.0f);
    glRectf(-1.0f, -1.0f, 1.0f, 1.0f);
    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(600, 300);
    glutCreateWindow("LCD Simulator");
    glutDisplayFunc(draw);
    glutMainLoop();
    return 0;
}
