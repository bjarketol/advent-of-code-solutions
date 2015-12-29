subroutine calculate_presents(house_no, target)
  implicit none
  integer, intent(in) :: target
  integer, intent(out) :: house_no
  integer :: presents, elf
  real :: lim

  lim = floor(sqrt(float(target))) + 2

  do house_no = 1, target
    presents = 0
    do elf = 1, int(lim)
      if (mod(house_no, elf) .eq. 0) then
        if (house_no .ge. elf) then
          presents = presents + elf
        end if
      end if
    end do
    !print*, house_no, presents
    if (presents .ge. target) then
      exit
    end if
  end do
  return
end subroutine
