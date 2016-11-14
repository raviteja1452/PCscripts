while true; do
    echo "Press Q to exit \t\t: "
    read input
    if [[ $input = "q" ]] || [[ $input = "Q" ]] 
        then break 
    else 
        echo "Invalid Input."
    fi
done