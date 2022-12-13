!(function (t, e) {
  "object" == typeof exports && "undefined" != typeof module
    ? (module.exports = e())
    : "function" == typeof define && define.amd
    ? define(e)
    : (t.iodine = e());
})(this, function () {
  var t = function () {
    this.messages = this._defaultMessages();
  };
  return (
    (t.prototype._dateCompare = function (t, e, r, i) {
      return (
        void 0 === i && (i = !1),
        !!this.isDate(t) &&
          !(!this.isDate(e) && !this.isInteger(e)) &&
          ((e = "number" == typeof e ? e : e.getTime()),
          "less" === r && i
            ? t.getTime() <= e
            : "less" !== r || i
            ? "more" === r && i
              ? t.getTime() >= e
              : "more" !== r || i
              ? void 0
              : t.getTime() > e
            : t.getTime() < e)
      );
    }),
    (t.prototype._defaultMessages = function () {
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
    }),
    (t.prototype.addRule = function (e, r) {
      t.prototype["is" + e[0].toUpperCase() + e.slice(1)] = r;
    }),
    (t.prototype.getErrorMessage = function (t, e) {
      void 0 === e && (e = void 0);
      var r = t.split(":")[0],
        i = e || t.split(":")[1];
      return (
        ["after", "afterOrEqual", "before", "beforeOrEqual"].includes(r) &&
          (i = new Date(parseInt(i)).toLocaleTimeString(void 0, {
            year: "numeric",
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "numeric",
          })),
        [null, void 0].includes(i)
          ? this.messages[r]
          : this.messages[r].replace("[PARAM]", i)
      );
    }),
    (t.prototype.isAfter = function (t, e) {
      return this._dateCompare(t, e, "more", !1);
    }),
    (t.prototype.isAfterOrEqual = function (t, e) {
      return this._dateCompare(t, e, "more", !0);
    }),
    (t.prototype.isArray = function (t) {
      return Array.isArray(t);
    }),
    (t.prototype.isBefore = function (t, e) {
      return this._dateCompare(t, e, "less", !1);
    }),
    (t.prototype.isBeforeOrEqual = function (t, e) {
      return this._dateCompare(t, e, "less", !0);
    }),
    (t.prototype.isBoolean = function (t) {
      return [!0, !1].includes(t);
    }),
    (t.prototype.isDate = function (t) {
      return (
        t && "[object Date]" === Object.prototype.toString.call(t) && !isNaN(t)
      );
    }),
    (t.prototype.isDifferent = function (t, e) {
      return t != e;
    }),
    (t.prototype.isEndingWith = function (t, e) {
      return this.isString(t) && t.endsWith(e);
    }),
    (t.prototype.isEmail = function (t) {
      return new RegExp("^\\S+@\\S+[\\.][0-9a-z]+$").test(
        String(t).toLowerCase()
      );
    }),
    (t.prototype.isFalsy = function (t) {
      return [0, "0", !1, "false"].includes(t);
    }),
    (t.prototype.isIn = function (t, e) {
      return (e = "string" == typeof e ? e.split(",") : e).includes(t);
    }),
    (t.prototype.isInteger = function (t) {
      return Number.isInteger(t) && parseInt(t).toString() === t.toString();
    }),
    (t.prototype.isJson = function (t) {
      try {
        return "object" == typeof JSON.parse(t);
      } catch (t) {
        return !1;
      }
    }),
    (t.prototype.isMaximum = function (t, e) {
      return (t = "string" == typeof t ? t.length : t), parseFloat(t) <= e;
    }),
    (t.prototype.isMinimum = function (t, e) {
      return (t = "string" == typeof t ? t.length : t), parseFloat(t) >= e;
    }),
    (t.prototype.isNotIn = function (t, e) {
      return !this.isIn(t, e);
    }),
    (t.prototype.isNumeric = function (t) {
      return !isNaN(parseFloat(t)) && isFinite(t);
    }),
    (t.prototype.isOptional = function (t) {
      return [null, void 0, ""].includes(t);
    }),
    (t.prototype.isRegexMatch = function (t, e) {
      return new RegExp(e).test(String(t).toLowerCase());
    }),
    (t.prototype.isRequired = function (t) {
      return !this.isOptional(t);
    }),
    (t.prototype.isSame = function (t, e) {
      return t == e;
    }),
    (t.prototype.isStartingWith = function (t, e) {
      return this.isString(t) && t.startsWith(e);
    }),
    (t.prototype.isString = function (t) {
      return "string" == typeof t;
    }),
    (t.prototype.isTruthy = function (t) {
      return [1, "1", !0, "true"].includes(t);
    }),
    (t.prototype.isUrl = function (t) {
      return new RegExp(
        "^(https?:\\/\\/)?((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|((\\d{1,3}\\.){3}\\d{1,3}))(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*(\\?[;&a-z\\d%_.~+=-]*)?(\\#[-a-z\\d_]*)?$"
      ).test(String(t).toLowerCase());
    }),
    (t.prototype.isUuid = function (t) {
      return new RegExp(
        "^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
      ).test(String(t).toLowerCase());
    }),
    (t.prototype.is = function (t, e) {
      if ((void 0 === e && (e = []), 0 === e.length)) return !0;
      if ("optional" === e[0] && this.isOptional(t)) return !0;
      for (var r = 0; r < e.length; r++)
        if (
          "optional" !== e[r] &&
          !this[
            "is" +
              (e[r].split(":")[0][0].toUpperCase() +
                e[r].split(":")[0].slice(1))
          ].apply(this, [t, e[r].split(":")[1]])
        )
          return e[r];
      return !0;
    }),
    (t.prototype.setErrorMessages = function (t) {
      this.messages = t;
    }),
    (window.Iodine = new t()),
    t
  );
});
