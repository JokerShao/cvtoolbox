	/************************************************************************/
	/*   2 基础定位四元数转MaYa欧拉角      XYZ旋转顺序                         */
	/************************************************************************/
	static TransformDataEuler convertToMayaTrans(const TransformData& optical_center)
	{
		Eigen::Quaterniond Qcr = Eigen::Quaterniond(optical_center.orientation[0], optical_center.orientation[1], optical_center.orientation[2], optical_center.orientation[3]);
		Eigen::Vector3d Tcr = Eigen::Vector3d(optical_center.position[0], optical_center.position[1], optical_center.position[2]);
		Eigen::Quaterniond q = Qcr;
		Eigen::Matrix3d dcm;
		dcm << 0.0, 0.0, -1.0,
			0.0, 1.0, 0.0,
			1.0, 0.0, 0.0;
		Eigen::Quaterniond Qd = Eigen::Quaterniond(dcm);
		q = q * Qd;

		//ZYX旋转顺序(RPY角的XYZ)
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

		Eigen::Vector3d E;  // x:pitch;y:yaw;z:roll
		float R = r13;
		if (R > 0.99999)
		{
			R = R > 1 ? 1 : R;
			E.x() = 2 * atan2(q.z(), q.y());
			E.z() = 0;
			E.y() = asin(R);
			if (E.x() > PI)
				E.x() -= 2 * PI;
			else if (E.x() < -PI)
				E.x() += 2 * PI;
		}
		else if (R < -0.99999)
		{
			R = R < (-1) ? (-1) : R;
			E.x() = 2 * atan2(q.z(), q.y());
			E.z() = 0;
			E.y() = asin(R);
			if (E.x() > PI)
				E.x() -= 2 * PI;
			else if (E.x() < -PI)
				E.x() += 2 * PI;
		}
		else
		{
			E.x() = atan2(r23, r33);   //pitch  
			E.y() = asin(-r13);          //yaw    
			E.z() = atan2(r12, r11);   //roll   
		}

		Eigen::Vector3d Euler = E * 180 / PI;

		static Eigen::Vector3d Elast = Eigen::Vector3d(0, 0, 0);
		if (!(Elast == Eigen::Vector3d(0, 0, 0)))
		{
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
			//Z
			if (Elast.z() > -180 && Elast.z() < 180)
			{
				if (abs(Euler.z() - Elast.z()) > 180 && Euler.z()*Elast.z() < 0)
				{
					Euler.z() = Euler.z() > 0 ? Euler.z() - 360 : Euler.z() + 360;
				}
			}
			else
			{
				while (abs(Euler.z() - Elast.z()) > 180)
				{
					Euler.z() = Elast.z() > 0 ? Euler.z() + 360 : Euler.z() - 360;
				}
			}
		}
		Elast = Euler;

		return TransformDataEuler{ Tcr.x(), Tcr.y(), Tcr.z(), Euler.x(), Euler.y(), Euler.z() };
	}