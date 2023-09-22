set -eu

all_tests_succeeded=true
for ((i = 1; i <= 10; i++)); do
    input_file="tests/$i.in"
    output_file="tests/$i.out"

    program_output=$(solutions/go.run <"$input_file")
    expected_output=$(cat "$output_file")

    if [ "$program_output" != "$expected_output" ]; then
        echo "Test $i failed:"
        echo "Program output:"
        echo "$program_output"
        echo "Expected output:"
        echo "$expected_output"
        all_tests_succeeded=false
    fi
done

if [ "$all_tests_succeeded" = true ]; then
    echo "All tests succeeded."
    exit 0 # Exit with a success status
else
    echo "One or more tests failed."
    exit 1 # Exit with a failure status
fi
