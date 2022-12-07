/*
|--------------------------------------------------------------------------
| Iodine - JavaScript Library
|--------------------------------------------------------------------------
|
| This library contains a collection of useful validation rules that can
| be used to quickly verify whether items meet certain conditions.
|
*/
class Iodine {
    /**
     * Constructor.
     *
     **/
    constructor() {
      this.locale = undefined;
      this.messages = this._defaultMessages();
    }
  
    /**
     * @internal.
     *
     **/
    _dateCompare(first, second, type, equals = false) {
      if (!this.isDate(first)) return false;
  
      if (!this.isDate(second) && !this.isInteger(second)) return false;
  
      second = typeof second === "number" ? second : second.getTime();
  
      if (type === "less" && equals) return first.getTime() <= second;
      if (type === "less" && !equals) return first.getTime() < second;
      if (type === "more" && equals) return first.getTime() >= second;
      if (type === "more" && !equals) return first.getTime() > second;
    }
  
    /**
     * @internal.
     *
     **/
    _defaultMessages() {
      return {
        after: `时间必须在: '[PARAM]'之后`,
        afterOrEqual: `时间必须等于或者在: '[PARAM]'之后`,
        array: `值必须是数组`,
        before: `时间必须在: '[PARAM]'之前`,
        beforeOrEqual: `时间必须等于或者在: '[PARAM]'之前`,
        boolean: `值必须是true或false`,
        date: `值必须是时间`,
        different: `值必须是与 '[PARAM]' 不同`,
        endingWith: `Value must end with '[PARAM]'`,
        email: `值必须是有效的电子邮箱格式`,
        falsy: `必须为假值 (false, 'false', 0 or '0')`,
        in: `必须是以下选项之一: [PARAM]`,
        integer: `值必须是整数`,
        json: `Value must be a parsable JSON object string`,
        maximum: `值的大小或字符长度不能大于'[PARAM]'`,
        minimum: `值的大小或字符长度不能小于'[PARAM]'`,
        notIn: `值不能是以下选项之一: [PARAM]`,
        numeric: `必须为数字`,
        optional: `值是可选的`,
        regexMatch: `值必须满足正则表达式: [PARAM]`,
        required: `必须填写`,
        same: `值必须是 '[PARAM]'`,
        startingWith: `值必须以 '[PARAM]'`,
        string: `值必须为字符串`,
        truthy: `必须为真值(true, 'true', 1 or '1')`,
        url: `值必须是一个有效的url`,
        uuid: `值必须是一个有效 UUID`,
      };
    }
  
    /**
     * Attach a custom validation rule to the library.
     *
     **/
    addRule(name, closure) {
      Iodine.prototype[`is${name[0].toUpperCase()}${name.slice(1)}`] = closure;
    }
  
    /**
     * Retrieve an error message for the given rule.
     *
     **/
    getErrorMessage(rule, arg = undefined) {
      let key = rule.split(":")[0];
      let param = arg || rule.split(":")[1];
  
      if (["after", "afterOrEqual", "before", "beforeOrEqual"].includes(key)) {
        param = new Date(parseInt(param)).toLocaleTimeString(this.locale, {
          year: "numeric",
          month: "short",
          day: "numeric",
          hour: "2-digit",
          minute: "numeric",
        });
      }
  
      return [null, undefined].includes(param)
        ? this.messages[key]
        : this.messages[key].replace("[PARAM]", param);
    }
  
    /**
     * Determine if the given date is after another given date.
     *
     **/
    isAfter(value, after) {
      return this._dateCompare(value, after, "more", false);
    }
  
    /**
     * Determine if the given date is after or equal to another given date.
     *
     **/
    isAfterOrEqual(value, after) {
      return this._dateCompare(value, after, "more", true);
    }
  
    /**
     * Determine if the given value is an array.
     *
     **/
    isArray(value) {
      return Array.isArray(value);
    }
  
    /**
     * Determine if the given date is before another given date.
     *
     **/
    isBefore(value, before) {
      return this._dateCompare(value, before, "less", false);
    }
  
    /**
     * Determine if the given date is before or equal to another given date.
     *
     **/
    isBeforeOrEqual(value, before) {
      return this._dateCompare(value, before, "less", true);
    }
  
    /**
     * Determine if the given value is a boolean.
     *
     **/
    isBoolean(value) {
      return [true, false].includes(value);
    }
  
    /**
     * Determine if the given value is a date object.
     *
     **/
    isDate(value) {
      return (
        value &&
        Object.prototype.toString.call(value) === "[object Date]" &&
        !isNaN(value)
      );
    }
  
    /**
     * Determine if the given value is different to another given value.
     *
     **/
    isDifferent(value, different) {
      return value != different;
    }
  
    /**
     * Determine if the given value ends with another given value.
     *
     **/
    isEndingWith(value, sub) {
      return this.isString(value) && value.endsWith(sub);
    }
  
    /**
     * Determine if the given value is a valid email address.
     *
     **/
    isEmail(value) {
      return new RegExp("^\\S+@\\S+[\\.][0-9a-z]+$").test(
        String(value).toLowerCase()
      );
    }
  
    /**
     * Determine if the given value is falsy.
     *
     **/
    isFalsy(value) {
      return [0, "0", false, "false"].includes(value);
    }
  
    /**
     * Determine if the given value is within the given array of options.
     *
     **/
    isIn(value, options) {
      options = typeof options === "string" ? options.split(",") : options;
  
      return options.includes(value);
    }
  
    /**
     * Determine if the given value is an integer.
     *
     **/
    isInteger(value) {
      return (
        Number.isInteger(value) && parseInt(value).toString() === value.toString()
      );
    }
  
    /**
     * Determine if the given value is a JSON string.
     *
     **/
    isJson(value) {
      try {
        return typeof JSON.parse(value) === "object";
      } catch (e) {
        return false;
      }
    }
  
    /**
     * Determine if the given value meets the given maximum limit.
     *
     **/
    isMaximum(value, limit) {
      value = typeof value === "string" ? value.length : value;
  
      return parseFloat(value) <= limit;
    }
  
    /**
     * Determine if the given value meets the given minimum limit.
     *
     **/
    isMinimum(value, limit) {
      value = typeof value === "string" ? value.length : value;
  
      return parseFloat(value) >= limit;
    }
  
    /**
     * Determine if the given value is not within the given array of options.
     *
     **/
    isNotIn(value, options) {
      return !this.isIn(value, options);
    }
  
    /**
     * Determine if the given value is numeric (an integer or a float).
     *
     **/
    isNumeric(value) {
      return !isNaN(parseFloat(value)) && isFinite(value);
    }
  
    /**
     * Determine if the given value is optional.
     *
     **/
    isOptional(value) {
      return [null, undefined, ""].includes(value);
    }
  
    /**
     * Determine if the given value satisifies the given regular expression.
     *
     **/
    isRegexMatch(value, expression) {
      return new RegExp(expression).test(String(value));
    }
  
    /**
     * Determine if the given value is present.
     *
     **/
    isRequired(value) {
      return !this.isOptional(value);
    }
  
    /**
     * Determine if the given value is the same as another given value.
     *
     **/
    isSame(value, same) {
      return value == same;
    }
  
    /**
     * Determine if the given value starts with another given value.
     *
     **/
    isStartingWith(value, sub) {
      return this.isString(value) && value.startsWith(sub);
    }
  
    /**
     * Determine if the given value is a string.
     *
     **/
    isString(value) {
      return typeof value === "string";
    }
  
    /**
     * Determine if the given value is truthy.
     *
     **/
    isTruthy(value) {
      return [1, "1", true, "true"].includes(value);
    }
  
    /**
     * Determine if the given value is a valid URL.
     *
     **/
    isUrl(value) {
      return new RegExp(
        "^(https?:\\/\\/)?((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|((\\d{1,3}\\.){3}\\d{1,3}))(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*(\\?[;&a-z\\d%_.~+=-]*)?(\\#[-a-z\\d_]*)?$"
      ).test(String(value).toLowerCase());
    }
  
    /**
     * Determine if the given value is a valid UUID.
     *
     **/
    isUuid(value) {
      return new RegExp(
        "^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
      ).test(String(value).toLowerCase());
    }
  
    /**
     * Determine whether the given value meets the given rules.
     *
     **/
    is(value, rules = []) {
      if (!rules.length) return true;
  
      if (rules[0] === "optional" && this.isOptional(value)) return true;
  
      for (let index in rules) {
        if (rules[index] === "optional") continue;
  
        let rule =
          rules[index].split(":")[0][0].toUpperCase() +
          rules[index].split(":")[0].slice(1);
  
        let result = this[`is${rule}`].apply(this, [
          value,
          rules[index].split(":")[1],
        ]);
  
        if (!result) return rules[index];
      }
  
      return true;
    }
  
    /**
     * Replace the default error messages with a new set.
     *
     **/
    setErrorMessages(messages) {
      this.messages = messages;
    }
  
    /**
     * Replace the default locale with a new value.
     *
     **/
    setLocale(locale) {
      this.locale = locale;
    }
  }
  
  /**
   * Create an instance of the library.
   *
   **/
  
  export default new Iodine();
  
  //window.Iodine = new Iodine();
  