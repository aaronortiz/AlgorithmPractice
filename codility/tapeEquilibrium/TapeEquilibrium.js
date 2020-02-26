module.exports = class TapeEquilibrium {
    solution(A) {
        // write your code in JavaScript (Node.js 8.9.4)
        if (A.length < 2) {
            return 0;
        } else {

            var leftIndex = 0;
            var rightIndex = A.length - 1;
            var leftSum = A[leftIndex];
            var rightSum = A[rightIndex];
            var visitedIndices = 2;

            while (visitedIndices < A.length) {

                var nextLeftSum = leftSum + A[leftIndex + 1];
                var nextRightSum = rightSum + A[rightIndex - 1];
                var nextLeftDiff = Math.abs(nextLeftSum - rightSum);
                var nextRightDiff = Math.abs(leftSum - nextRightSum);

                if (nextLeftDiff < nextRightDiff) {
                    leftIndex++;
                    leftSum += A[leftIndex];
                } else {
                    rightIndex--;
                    rightSum += A[rightIndex];
                }
                visitedIndices++;
            }
        }

        return Math.abs(leftSum - rightSum);

    }
}