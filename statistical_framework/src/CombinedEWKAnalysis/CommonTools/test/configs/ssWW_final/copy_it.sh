for j in 0 1 2 3 4
do
  for i in fs0 fs1 fm1 fm7 ft0 ft1 ft2
    do
      cp ./ssWW_final_fm0_${j}_config ./ssWW_final_${i}_${j}_config
    done
  for i in fs0 fs1 fm1 fm7 ft0 ft1 ft2
    do
      sed -i 's/fm0/'${i}'/g' *${i}_${j}_config
    done
done

