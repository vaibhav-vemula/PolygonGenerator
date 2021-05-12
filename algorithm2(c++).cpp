#include <iostream>
using namespace std;
#include <math.h>

#include <random>


struct Point
{
	int x, y;
};

void generatePolygon(int ctrX, int ctrY, int aveRadius, float irregularity, float spikeyness, int numVerts ){


    std::default_random_engine generator;
    std::normal_distribution<double> distribution(aveRadius,spikeyness);

    irregularity =  irregularity * 2*M_PI / numVerts;
    spikeyness = spikeyness * aveRadius;

    float lower = (2*M_PI / numVerts) - irregularity;
    float upper = (2*M_PI / numVerts) + irregularity;
    float sum = 0;
     
    float angleSteps[1000];

    

    for(int i=0;i<=numVerts;i++){
        
        float tmp = lower + (float)(rand()) / ((float)(RAND_MAX/(upper - lower)));
        angleSteps[i] = tmp;
        sum = sum+ tmp;
        
        
    }
    
   float k = sum / (2*M_PI);
   for(int y=0;y<=numVerts;y++){
       angleSteps[y] = angleSteps[y] / k;
   }
    
    Point points[1000];

    float angle = (float)(rand()) / ((float)(RAND_MAX/(2*M_PI)));

    for(int j = 0; j<=numVerts;j++){
        float r_i =  distribution(generator);
        float x,y;
        x =  ctrX + r_i*cos(angle);
        y = ctrY + r_i*sin(angle);

        points[j].x=(int)x;
        points[j].y=(int)y;
        angle = angle+angleSteps[j];
    }


    // for (int i=0; i<numVerts; i++)
	// cout << "(" << points[i].x << ", "
	// 		<< points[i].y <<"), ";



}

int main() 
{

    int ctrX=100, ctrY=100, aveRadius=200,numVerts=200; 
    float irregularity=1, spikeyness=0.11;
    for(int tm = 0; tm<1000;tm++){

        numVerts = rand() % 500 +1;
        generatePolygon(ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts);
    }
    return 0;
}
