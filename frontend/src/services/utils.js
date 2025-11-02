/*
Utility functions to be used across pages.
*/

export function updateIsTraining(value) {
    localStorage.setItem("isTraining", value.toString());
    window.dispatchEvent(new Event("training-update"));
}

// Polls for the validation status from the backend
export const pollValidationStatus = async (apiService) => {
    const POLLING_INTERVAL = 10_000;
    const MAX_RETRIES = 180;

    let retries = 0;

    while (retries < MAX_RETRIES) {
        try {
            const res = await apiService.getValidationStatus();
            console.log("Polling validation response:", res);

            if (res && res.status === "complete") {
                return true;
            }

            if (res && res.status === "pending") {
                await new Promise((r) => setTimeout(r, POLLING_INTERVAL));
                retries++;
                continue;
            }

            throw new Error("Unexpected response while polling validation result.");

        } catch (err) {
            console.error("Polling error:", err);
            throw err;
        }
    }

    console.warn("Polling timed out waiting for validation result.");
    throw new Error("Timed out waiting for validation result");
};

// Polls for the training status from the backend
export const pollTrainingStatus = async (apiService) => {
    const POLLING_INTERVAL = 10_000;
    const MAX_RETRIES = 180;

    let retries = 0;

    while (retries < MAX_RETRIES) {
        try {
            const res = await apiService.getTrainingStatus();
            console.log("Polling training response:", res);

            if (res && res.status === "complete") {
                return res;
            }

            if (res && res.status === "pending") {
                await new Promise((r) => setTimeout(r, POLLING_INTERVAL));
                retries++;
                continue;
            }

            throw new Error("Unexpected response while polling training result.");

        } catch (err) {
            console.error("Polling error:", err);
            throw err;
        }
    }

    console.warn("Polling timed out waiting for training result.");
    throw new Error("Timed out waiting for training result");
};

// Logging functions
export const log = (...args) => {
  if (import.meta.env.DEV) {
    console.log(...args);
  }
};

export const warn = (...args) => {
  if (import.meta.env.DEV) {
    console.warn(...args);
  }
};

export const err = (...args) => {
  // Logs all errors regardless of environment
  console.error(...args);
};