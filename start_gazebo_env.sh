roslaunch gazebo_ros empty_world.launch paused:=true use_sim_time:=false gui:=true throttled:=false recording:=false debug:=true public_sim:=true &

sleep 1

echo "Init /robot_description param"
rosparam set /robot_description "$(xacro 'src/motoman/motoman_hc10_support/urdf/hc10.xacro')"
echo "Done"
