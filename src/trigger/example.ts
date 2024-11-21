import { logger, task } from "@trigger.dev/sdk/v3";
import { BedrockAgentRuntimeClient, RetrieveCommand } from "@aws-sdk/client-bedrock-agent-runtime";

// init Bedrock client
const bedrockClient = new BedrockAgentRuntimeClient({
  region: process.env.AWS_REGION,
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY ?? "",
  },
});

// define the task
export const sendPromptToBedrock = task({
  id: "send-prompt-to-bedrock",
  run: async (payload: { kbId: string; query: string }) => {
    try {
      logger.log("Sending prompt to Bedrock model", payload);

      const input = {
        knowledgeBaseId: process.env.KB_ID, // specify the Knowledge Base ID
        retrievalQuery: { 
          text: payload.query,
        },
      };

      // create the command
      const command = new RetrieveCommand(input);

      // send the request to Bedrock
      const response = await bedrockClient.send(command);

      return response; 
    } catch (error) {
      logger.error("Error invoking Bedrock model", { error });
      throw error;
    }
  },
});
