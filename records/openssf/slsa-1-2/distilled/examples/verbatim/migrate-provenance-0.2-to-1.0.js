{
    "buildDefinition": {
        // The `buildType` MUST be updated for v1.0 to describe how to
        // interpret `inputArtifacts`.
        "buildType": /* updated version of */ old.buildType,
        "externalParameters":
            old.invocation.parameters + {
            // It is RECOMMENDED to rename "entryPoint" to something more
            // descriptive.
            "entryPoint": old.invocation.configSource.entryPoint,
            // It is OPTIONAL to rename "source" to something more descriptive,
            // especially if "source" is ambiguous or confusing.
            "source": old.invocation.configSource.uri,
        },
        "internalParameters": old.invocation.environment,
        "resolvedDependencies":
            old.materials + [
            {
                "uri": old.invocation.configSource.uri,
                "digest": old.invocation.configSource.digest,
            }
        ]
    },
    "runDetails": {
        "builder": {
            "id": old.builder.id,
            "builderDependencies": null,  // not in v0.2
            "version": null,  // not in v0.2
        },
        "metadata": {
            "invocationId": old.metadata.buildInvocationId,
            "startedOn": old.metadata.buildStartedOn,
            "finishedOn": old.metadata.buildFinishedOn,
        },
        "byproducts": null,  // not in v0.2
    },
}
