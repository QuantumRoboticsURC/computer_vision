// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/FollowGPS.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__FOLLOW_GPS__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__FOLLOW_GPS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/FollowGPS in the package custom_interfaces.
typedef struct custom_interfaces__srv__FollowGPS_Request
{
  double latitude;
  double longitude;
} custom_interfaces__srv__FollowGPS_Request;

// Struct for a sequence of custom_interfaces__srv__FollowGPS_Request.
typedef struct custom_interfaces__srv__FollowGPS_Request__Sequence
{
  custom_interfaces__srv__FollowGPS_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__FollowGPS_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/FollowGPS in the package custom_interfaces.
typedef struct custom_interfaces__srv__FollowGPS_Response
{
  bool arrived;
} custom_interfaces__srv__FollowGPS_Response;

// Struct for a sequence of custom_interfaces__srv__FollowGPS_Response.
typedef struct custom_interfaces__srv__FollowGPS_Response__Sequence
{
  custom_interfaces__srv__FollowGPS_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__FollowGPS_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__FOLLOW_GPS__STRUCT_H_
