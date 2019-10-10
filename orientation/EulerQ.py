Eigen::Vector3d CPOLY::QtoEuler(Eigen::Quaterniond q, EulerMode Mode)
{
    //四元数转欧拉角
	double r11, r12, r13, r21, r22, r23, r31, r32, r33;
	r11 = q.w() * q.w() + q.x() * q.x() - q.y() * q.y() - q.z()*q.z();
	r12 = 2 * (q.x() * q.y() + q.w() * q.z());
	r13 = 2 * (q.x() * q.z() - q.w() * q.y());
	r21 = 2 * (q.x() * q.y() - q.w() * q.z());
	r22 = q.w() * q.w() - q.x() * q.x() + q.y() * q.y() - q.z()*q.z();
	r23 = 2 * (q.y() * q.z() + q.w() * q.x());
	r31 = 2 * (q.x() * q.z() + q.w() * q.y());
	r32 = 2 * (q.y() * q.z() - q.w() * q.x());
	r33 = q.w() * q.w() - q.x() * q.x() - q.y() * q.y() + q.z()*q.z();

	Vector3d E;  // x:pitch;y:yaw;z:roll
	float R;
	if (Mode == ZYX)
	{
		R = r13;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = 2 * atan2(q.x(), q.w());
			E.y() = asin(R);
			E.z() = 0;
			if (E.x() > PI) {E.x() -= 2 * PI;}				
			else if (E.x() < -PI) {E.x() += 2 * PI;}
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = 2 * atan2(q.x(), q.w());
			E.y() = asin(R);
			E.z() = 0;
			if (E.x() > PI) {E.x() -= 2 * PI;}				
			else if (E.x() < -PI) {E.x() += 2 * PI;}				
		}
		else
		{
			E.x() = atan2(r23, r33);   //pitch  
			E.y() = asin(-r13);          //yaw    
			E.z() = atan2(r12, r11);   //roll   
		}
	}
	if (Mode == XYZ)
	{
		R = r31;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = 2 * atan2(q.x(), q.w());
			E.y() = asin(R);
			E.z() = 0;
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = 2 * atan2(q.x(), q.w());
			E.y() = asin(R);
			E.z() = 0;
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else
		{
			E.x() = atan2(-r32, r33);   //pitch  
			E.y() = asin(r31);          //yaw    
			E.z() = atan2(-r21, r11);   //roll   
		}
	}
	if (Mode == ZXY)
	{
		R = r23;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = asin(R);
			E.y() = 2 * atan2(q.y(), q.w());
			E.z() = 0;
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = asin(R);
			E.y() = 2 * atan2(q.y(), q.x());
			E.z() = 0;
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else
		{
			E.x() = asin(r23);                 //pitch  
			E.y() = atan2(-r13, r33);          //yaw    
			E.z() = atan2(-r21, r22);          //roll   
		}     
	}
	if (Mode == YXZ)
	{
		R = r32;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = asin(R);
			E.y() = 2 * atan2(q.y(), q.w());
			E.z() = 0;
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = asin(R);
			E.y() = 2 * atan2(q.y(), q.x());
			E.z() = 0;
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else
		{
			E.x() = asin(-r32);                 //pitch  
			E.y() = atan2(r31, r33);          //yaw    
			E.z() = atan2(r12, r22);          //roll   
		}
	}
	if (Mode == YZX)
	{
		R = r12;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = 0;
			E.y() = 2 * atan2(q.y(), q.z());
			E.z() = asin(R);
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = 0;
			E.y() = 2 * atan2(q.y(), q.z());
			E.z() = asin(R);
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else
		{
			E.x() = atan2(-r32, r22);   //pitch  
			E.y() = atan2(-r13, r11);          //yaw    
			E.z() = asin(r12);   //roll   
		}
	}
	if (Mode == XZY)
	{
		R = r12;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = 0;
			E.y() = 2 * atan2(q.y(), q.z());
			E.z() = asin(R);
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = 0;
			E.y() = 2 * atan2(q.y(), q.z());
			E.z() = asin(R);
			if (E.x() > PI) { E.x() -= 2 * PI; }
			else if (E.x() < -PI) { E.x() += 2 * PI; }
		}
		else
		{
			E.x() = atan2(r23, r22);         //pitch  
			E.y() = atan2(r31, r11);          //yaw    
			E.z() = asin(-r21);                //roll   
		}
	}
	Vector3d Euler = E * 180 / PI;

	return Euler;
}

Eigen::Quaterniond CPOLY::EulertoQ(Eigen::Vector3d Euler, EulerMode Mode)
{
    //欧拉角转四元数
	Vector3d E = Euler * PI / 180;
	//Pitch:E.x  Yaw:E.y   Roll:E.z
	double CP = cos(E.x() / 2);
	double SP = sin(E.x() / 2);
	double CY = cos(E.y() / 2);
	double SY = sin(E.y() / 2);
	double CR = cos(E.z() / 2);
	double SR = sin(E.z() / 2);

	Quaterniond Q;
	if (Mode == ZYX)
	{
		Q.w() = CP * CY * CR + SP * SY * SR;
		Q.x() = SP * CY * CR - CP * SY * SR;
		Q.y() = CP * SY * CR + SP * CY * SR;
		Q.z() = CP * CY * SR - SP * SY * CR;
	}
	if (Mode == XYZ)
	{
		Q.w() = CP * CY * CR - SP * SY * SR;
		Q.x() = SP * CY * CR + CP * SY * SR;
		Q.y() = CP * SY * CR - SP * CY * SR;
		Q.z() = CP * CY * SR + SP * SY * CR;
	}
	if (Mode == ZXY)
	{
		Q.w() = CP * CY * CR - SP * SY * SR;
		Q.x() = SP * CY * CR - CP * SY * SR;
		Q.y() = CP * SY * CR + SP * CY * SR;
		Q.z() = CP * CY * SR + SP * SY * CR;
	}
	if (Mode == YXZ)
	{
		Q.w() = CP * CY * CR + SP * SY * SR;
		Q.x() = SP * CY * CR + CP * SY * SR;
		Q.y() = CP * SY * CR - SP * CY * SR;
		Q.z() = CP * CY * SR - SP * SY * CR;
	}
	if (Mode == YZX)
	{
		Q.w() = CP * CY * CR - SP * SY * SR;
		Q.x() = SP * CY * CR + CP * SY * SR;
		Q.y() = CP * SY * CR + SP * CY * SR;
		Q.z() = CP * CY * SR - SP * SY * CR;
	}
	if (Mode == ZXY)
	{
		Q.w() = CP * CY * CR + SP * SY * SR;
		Q.x() = SP * CY * CR - CP * SY * SR;
		Q.y() = CP * SY * CR - SP * CY * SR;
		Q.z() = CP * CY * SR + SP * SY * CR;
	}
	
	Q.normalized();
	return Q;
}

Eigen::Vector3d CPOLY::EulerSM(Eigen::Vector3d E, Eigen::Vector3d El, EulerMode Mode)
{
    //欧拉角的连续性处理
	Vector3d Euler = E;
	Vector3d Elast = El;
	if (Mode == XYZ || Mode == ZYX)
	{
		Euler.y() = E.z();
		Elast.y() = El.z();
	}
	if (Mode == ZXY || Mode == YXZ)
	{
		Euler.x() = E.z();
		Elast.x() = El.z();
	}

	if (Elast.x() > -180 && Elast.x() < 180)
	{
		if (abs(Euler.x() - Elast.x()) > 180 && Euler.x()*Elast.x() < 0)
		{
			Euler.x() = Euler.x() > 0 ? Euler.x() - 360 : Euler.x() + 360;
		}
	}
	else
	{
		while (abs(Euler.x() - Elast.x()) > 180)
		{
			Euler.x() = Elast.x() > 0 ? Euler.x() + 360 : Euler.x() - 360;
		}
	}
	//Y
	if (Elast.y() > -180 && Elast.y() < 180)
	{
		if (abs(Euler.y() - Elast.y()) > 180 && Euler.y()*Elast.y() < 0)
		{
			Euler.y() = Euler.y() > 0 ? Euler.y() - 360 : Euler.y() + 360;
		}
	}
	else
	{
		while (abs(Euler.y() - Elast.y()) > 180)
		{
			Euler.y() = Elast.y() > 0 ? Euler.y() + 360 : Euler.y() - 360;
		}
	}

	if (Mode == XYZ || Mode == ZYX)
	{
		Euler.z() = Euler.y();
		Euler.y() = E.y();
	}
	if (Mode == ZXY || Mode == YXZ)
	{
		Euler.z() = Euler.x();
		Euler.x() = E.x();
	}
	return Euler;
}
