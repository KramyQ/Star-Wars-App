const Ajv = require("ajv");

const empireJsonSchema = {
  type: "object",
  properties: {
    countdown: { type: "integer", minimum: 0 },
    bounty_hunters: {
      type: "array",
      items: {
        type: "object",
        properties: {
          planet: { type: "string" },
          day: { type: "integer", minimum: 1 },
        },
        required: ["planet", "day"],
      },
    },
  },
  required: ["countdown", "bounty_hunters"],
};

export async function readFileAsText(file) {
  let result_base64 = await new Promise((resolve) => {
    let fileReader = new FileReader();
    fileReader.onload = () => resolve(fileReader.result);
    fileReader.readAsText(file);
  });
  return result_base64;
}

function IsJsonString(str) {
  try {
    JSON.parse(str);
  } catch (e) {
    return false;
  }
  return true;
}

export function validateEmpireJson(empireJson) {
  if (IsJsonString(empireJson)) {
    const ajv = new Ajv();
    return ajv.validate(empireJsonSchema, JSON.parse(empireJson));
  } else {
    return false;
  }
}
