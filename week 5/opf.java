class Solution {
    public boolean isNumber(String s) {
        String pattern = "^\\s*[+-]?((\\d+(\\.\\d*)?)|(\\.\\d+))([eE][+-]?\\d+)?\\s*$";
        return s != null && s.matches(pattern);
    }
}
