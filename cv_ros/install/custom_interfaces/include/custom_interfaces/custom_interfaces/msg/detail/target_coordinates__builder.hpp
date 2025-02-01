// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/TargetCoordinates.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__TARGET_COORDINATES__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__TARGET_COORDINATES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/target_coordinates__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_TargetCoordinates_longitude
{
public:
  explicit Init_TargetCoordinates_longitude(::custom_interfaces::msg::TargetCoordinates & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::TargetCoordinates longitude(::custom_interfaces::msg::TargetCoordinates::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::TargetCoordinates msg_;
};

class Init_TargetCoordinates_latitude
{
public:
  Init_TargetCoordinates_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TargetCoordinates_longitude latitude(::custom_interfaces::msg::TargetCoordinates::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_TargetCoordinates_longitude(msg_);
  }

private:
  ::custom_interfaces::msg::TargetCoordinates msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::TargetCoordinates>()
{
  return custom_interfaces::msg::builder::Init_TargetCoordinates_latitude();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__TARGET_COORDINATES__BUILDER_HPP_
