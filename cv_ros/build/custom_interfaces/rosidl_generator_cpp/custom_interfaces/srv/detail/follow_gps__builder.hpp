// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/FollowGPS.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__FOLLOW_GPS__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__FOLLOW_GPS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/follow_gps__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_FollowGPS_Request_longitude
{
public:
  explicit Init_FollowGPS_Request_longitude(::custom_interfaces::srv::FollowGPS_Request & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::srv::FollowGPS_Request longitude(::custom_interfaces::srv::FollowGPS_Request::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::FollowGPS_Request msg_;
};

class Init_FollowGPS_Request_latitude
{
public:
  Init_FollowGPS_Request_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FollowGPS_Request_longitude latitude(::custom_interfaces::srv::FollowGPS_Request::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_FollowGPS_Request_longitude(msg_);
  }

private:
  ::custom_interfaces::srv::FollowGPS_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::FollowGPS_Request>()
{
  return custom_interfaces::srv::builder::Init_FollowGPS_Request_latitude();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_FollowGPS_Response_arrived
{
public:
  Init_FollowGPS_Response_arrived()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::FollowGPS_Response arrived(::custom_interfaces::srv::FollowGPS_Response::_arrived_type arg)
  {
    msg_.arrived = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::FollowGPS_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::FollowGPS_Response>()
{
  return custom_interfaces::srv::builder::Init_FollowGPS_Response_arrived();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__FOLLOW_GPS__BUILDER_HPP_
