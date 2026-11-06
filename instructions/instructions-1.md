# LAB672: Ground agents in your business with an ontology in Fabric IQ

Follow this walkthrough to stage the Zava supply-chain data, create an ontology,
enrich it with the Ontology agent, and explore supply-chain risks and delivery
responses.

## Create the lab workspace

1. Open a browser. Browse to https://app.fabric.microsoft.com
2. Sign in with the credentials in your **Resources** tab.
3. Select **Workspaces** > **New workspace** and name it `FabricIQWorkspace`.
   If the name is not available, append your lab instance number, for example
   `FabricIQWorkspace-67082872`. Use your chosen name wherever these instructions
   refer to `FabricIQWorkspace`.
4. Expand **Advanced**. Under **Workspace type**, select **Fabric**, then select
   the capacity listed in your lab's **Resources** tab. Its name starts with
   `fabricperuser`. Do not leave the workspace on **Power BI Pro**: the setup
   notebook requires a Fabric capacity.
5. Select **Apply**. Use this workspace instead of **My workspace**; the workspace
   root must be empty before you import the notebook.
