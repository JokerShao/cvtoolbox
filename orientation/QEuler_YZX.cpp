

Eigen::Vector3d CPOLY::QtoEuler(Eigen::Quaterniond q)
{
	//YZX
	double r11, r12, r13, r22, r32;
	r11 = q.w() * q.w() + q.x() * q.x() - q.y() * q.y() - q.z()*q.z();
	r12 = 2 * (q.x() * q.y() + q.w() * q.z());
	r13 = 2 * (q.x() * q.z() - q.w() * q.y());
	r22 = q.w() * q.w() - q.x() * q.x() + q.y() * q.y() - q.z()*q.z();
	r32 = 2 * (q.y() * q.z() - q.w() * q.x());

	Vector3d E;  // x:pitch;y:yaw;z:roll
	if (r12 > 0.99999)
	{
		r12 = r12 > 1 ? 1 : r12;
		E.x() = 0;
		E.y() = 2 * atan2(q.x(), q.w());
		E.z() = asin(r12);
		if (E.y() > PI)
			E.y() -= 2 * PI;
		else if (E.y() < -PI)
			E.y() += 2 * PI;
	}
	else if (r12 < -0.99999)
	{
		r12 = r12 < (-1) ? (-1) : r12;
		E.x() = 0;
		E.y() = -2 * atan2(q.x(), q.w());
		E.z() = asin(r12);
		if (E.y() > PI)
			E.y() -= 2 * PI;
		else if (E.y() < -PI)
			E.y() += 2 * PI;
	}
	else
	{
		E.x() = atan2(-r32, r22); E.y() = atan2(-r13, r11); E.z() = asin(r12);
	}

	Vector3d Euler = E * 180 / PI;
	
	return Euler;
}

Eigen::Quaterniond CPOLY::EulertoQ(Eigen::Vector3d Euler)
{
	//YZX
	Vector3d E = Euler * PI / 180;
	//Pitch:E.x  Yaw:E.y   Roll:E.z
	double CP = cos(E.x() / 2);
	double SP = sin(E.x() / 2);
	double CY = cos(E.y() / 2); 
	double SY = sin(E.y() / 2);
	double CR = cos(E.z() / 2);
	double SR = sin(E.z() / 2);

	Quaterniond Q;
	Q.w() = CP * CY * CR - SP * SY * SR;
	Q.x() = SP * CY * CR + CP * SY * SR; 
	Q.y() = CP * SY * CR + SP * CY * SR;
	Q.z() = CP * CY * SR - SP * SY * CR;

	Q.normalized();
	return Q;
}





