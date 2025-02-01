// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/Age.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__AGE__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__AGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/age__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_Age_days
{
public:
  explicit Init_Age_days(::custom_interfaces::msg::Age & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::Age days(::custom_interfaces::msg::Age::_days_type arg)
  {
    msg_.days = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::Age msg_;
};

class Init_Age_months
{
public:
  explicit Init_Age_months(::custom_interfaces::msg::Age & msg)
  : msg_(msg)
  {}
  Init_Age_days months(::custom_interfaces::msg::Age::_months_type arg)
  {
    msg_.months = std::move(arg);
    return Init_Age_days(msg_);
  }

private:
  ::custom_interfaces::msg::Age msg_;
};

class Init_Age_years
{
public:
  Init_Age_years()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Age_months years(::custom_interfaces::msg::Age::_years_type arg)
  {
    msg_.years = std::move(arg);
    return Init_Age_months(msg_);
  }

private:
  ::custom_interfaces::msg::Age msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::Age>()
{
  return custom_interfaces::msg::builder::Init_Age_years();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__AGE__BUILDER_HPP_
