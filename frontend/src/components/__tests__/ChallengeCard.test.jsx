import React from "react";
import { render, screen } from "@testing-library/react";
import ChallengeCard from "../ChallengeCard";

const challenge = {
  id: 1,
  title: "Test Challenge",
  description: "A test challenge description.",
  difficulty: "Easy",
  subcategory: "AI-ML"
};

describe("ChallengeCard", () => {
  it("renders challenge title and description", () => {
    render(<ChallengeCard challenge={challenge} />);
    expect(screen.getByText("Test Challenge")).toBeInTheDocument();
    expect(screen.getByText("A test challenge description.")).toBeInTheDocument();
  });

  it("shows the correct difficulty badge", () => {
    render(<ChallengeCard challenge={challenge} />);
    expect(screen.getByText("Easy")).toBeInTheDocument();
  });
});
