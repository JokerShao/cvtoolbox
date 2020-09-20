/*
slambook chapter3, part7
problem 5, cpp implement */

#include <iostream>
#include "Eigen/Core"

int main(int argc, char** argv)
{
    std::cout<<"Hello world!\n";
 
    Eigen::MatrixXd aa = Eigen::MatrixXd::Random(10, 10);
    
    std::cout<<"aa:\n"<<aa<<"\n";
    
    aa.block(0, 0, 3, 3) = Eigen::Matrix3d::Identity();
    
    std::cout<<"aa:\n"<<aa<<"\n";
    
 
 
    return 0;
}

