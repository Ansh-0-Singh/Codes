
mov a, #59
mov r0, #69
add a,r0
mov 20h,  a
add a, #192
mov 21h, a
addc a,r0
mov 22h,a
subb a,r0
mov 23h,a
mov b, #12
mul ab
mov 24h, a
div ab
end